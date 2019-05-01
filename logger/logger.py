import abc

class Logger(abc.ABC):

    @abc.abstractmethod
    def _write_log(self, log_type, message):
        pass

    @abc.abstractmethod
    def console_handler(self, bool):
        pass

    def set_log_lvl(self, log_lvl):
        print(f"Change log_lvl from {self._log_lvl} to {log_lvl}")
        self._log_lvl = log_lvl
