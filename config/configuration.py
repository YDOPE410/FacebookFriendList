from dataclasses import dataclass

@dataclass()
class Configuration:
    login: str
    password: str
    path_to_driver: str
    path_to_save_logs: str
    console_log: bool
    log_lvl: int
    site: str
