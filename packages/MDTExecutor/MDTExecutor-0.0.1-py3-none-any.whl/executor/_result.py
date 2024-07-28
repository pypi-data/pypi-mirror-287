from dataclasses import dataclass


@dataclass
class Result:
    command: str
    stdout: str
    stderr: str
    returncode: str
    time: float
