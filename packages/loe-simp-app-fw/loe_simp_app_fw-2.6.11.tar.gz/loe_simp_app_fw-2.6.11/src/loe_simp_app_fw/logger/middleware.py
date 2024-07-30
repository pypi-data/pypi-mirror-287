from multiprocessing import Event, JoinableQueue
from typing import Callable, List
from multiprocessing.synchronize import Event as EventType

from .backend_m import Backend as BackendM
from .backend_s import Backend as BackendS
from .model import Backend, Exceptions, LogEntry, LogLevelsE, ResourceLocator, LogLevels

class Middleware:
    def __init__(
        self,
        *args,
        **kwargs,
        ) -> None:
        self.log: Callable[[LogEntry], None] = self._log_list

        self.logs: List[LogEntry] = []
        self.backend_m: BackendM
        self.backend_s: BackendS
        self._current_backend: Backend = "NONE"

        self.log = self._log_list

        self.queue: JoinableQueue = JoinableQueue()
        self.isFinish: EventType = Event()

        self._directory: ResourceLocator
        self._level: LogLevels
        self._write_interval: float
        self._debug_log_length: int
        self._isSetUp: bool = False

    def _log_list(self, log: LogEntry) -> None:
        self.logs.append(log)
        print(log, end="")
        return

    def _log_backend_m(self, log: LogEntry) -> None:
        self.backend_m.log(log)
        return

    def _log_backend_s(self, log: LogEntry) -> None:
        self.queue.put(log)
        return

    def setup(
        self,
        log_directory: ResourceLocator, 
        log_level: LogLevels, 
        *args, 
        write_interval: float = 5.0, 
        debug_log_length: int = 5000, 
        **kwargs
        ) -> None:
        if self._isSetUp:
            self.log(
                LogEntry(
                    LogLevelsE.ERROR.name,
                    "Setup happens twice"
                )
            )
            raise Exceptions.DuplicatedBootstrap

        self._directory = log_directory
        self._level = log_level
        self._write_interval = write_interval
        self._debug_log_length = debug_log_length

        self._isSetUp = True

    def switch_none_to_backend_s(
        self, 
        ) -> None:
        """
        Bootstrap the middleware
        """
        if hasattr(self, "backend_s"):
            self.log(
                LogEntry(
                    LogLevelsE.ERROR.name,
                    "A backend in separate process already exists"
                )
            )
            raise Exceptions.DuplicatedBootstrap

        self._judge_backend("NONE")

        # Setup the new backend
        self.backend_s = BackendS(
            log_directory=self._directory,
            log_level=self._level,
            log_queue=self.queue,
            isFinish=self.isFinish,
            write_interval=self._write_interval,
            debug_log_length=self._debug_log_length,
        )
        self.log = self._log_backend_s
        # Start multiprocessing backend
        self.backend_s.start()
        self._current_backend = "SEPARATE"

        self.log(
            LogEntry(
                LogLevelsE.INFO.name,
                "Creating backend in separate process complete"
            )
        )

        # Load logs into queue
        [self.log(i) for i in self.logs]
        # Clean instance logs
        self.logs = []

        self.log(
            LogEntry(
                LogLevelsE.INFO.name,
                "Clean up instance logs complete"
            )
        )

    def switch_backend_s_to_backend_m(
        self,
        ) -> None:
        """
        Prepare to terminate the middleware
        """
        if not hasattr(self, "backend_s"):
            self.log(
                LogEntry(
                    LogLevelsE.ERROR.name,
                    "A backend in separate process does not exist"
                )
            )
            raise Exceptions.NoBackendFound

        self._judge_backend("SEPARATE")
        
        # Stop the old backend
        self.isFinish.set()
        self.backend_s.join()

        self.log(
            LogEntry(
                LogLevelsE.INFO.name,
                "Stopping backend in separate process complete"
            )
        )

        # Setup the new backend
        self.backend_m = BackendM(
            log_directory=self._directory,
            log_level=self._level,
            write_interval=self._write_interval,
            debug_log_length=self._debug_log_length
        )
        self.log = self._log_backend_m

        self._current_backend = "MAIN"
        
        # Deal with items left in queue
        if self.logs:
            print("Logs is not empty during switch, something terribly wrong happened")
            raise Exceptions.QueueCorruption

        self.log(
            LogEntry(
                LogLevelsE.INFO.name,
                "Switching backend to main thread complete"
            )
        )

        while not self.queue.empty():
            self.log(self.queue.get_nowait())
            self.queue.task_done()

        self.log(
            LogEntry(
                LogLevelsE.INFO.name,
                f"Clean up queue complete, testing if queue is now empty, {self.queue.empty()}"
            )
        )
        
        self.queue.join()

    def shutdown(self) -> None:
        self.switch_backend_s_to_backend_m()
        if self.backend_s.is_alive():
            self.log(
                LogEntry(
                    LogLevelsE.ERROR.name,
                    "Backend in separate process is still alive"
                )
            )
            raise Exceptions.BackendProcessNotDead

        self._judge_backend("MAIN")
        
        self.backend_m.finish()
        self.log(
            LogEntry(
                LogLevelsE.INFO.name,
                "All file backend shutdown, logs no longer save to file"
            )
        )
        self._current_backend = "NONE"

    def _judge_backend(self, expected: Backend) -> None:
        if self._current_backend != expected:
            self.log(
                LogEntry(
                    LogLevelsE.ERROR.name,
                    f"Invalid switching backend, current backend {self._current_backend}, expecting {expected}"
                )
            )
            raise Exceptions.InvalidBackendSwitch