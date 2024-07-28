from subprocess import Popen, PIPE
from typing import List, Dict, Any

from executor._base_executor import BaseExecutor
from dataclasses import dataclass
from shlex import join
import time

from executor._result import Result


@dataclass
class SubProcessExecutor(BaseExecutor):
    args: List[str]
    env: Dict[str, Any] | None = None

    def executor(self) -> Result | None:
        with Popen(args=self.args, env=self.env, stderr=PIPE, stdout=PIPE) as process:
            start_time = time.time()
            stdout, stderr = process.communicate()
            end_time = time.time()
            result = Result(
                command=join(self.args),
                stdout=stdout.decode("utf-8"),
                stderr=stderr.decode("utf-8"),
                returncode=process.returncode,
                time=end_time - start_time,
            )
        return result
