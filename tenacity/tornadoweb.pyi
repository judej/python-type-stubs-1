from tenacity import BaseRetrying as BaseRetrying, DoAttempt as DoAttempt, DoSleep as DoSleep, RetryCallState as RetryCallState
from typing import Any

class TornadoRetrying(BaseRetrying):
    sleep: Any = ...
    def __init__(self, sleep: Any = ..., **kwargs: Any) -> None: ...
    def call(self, fn: Any, *args: Any, **kwargs: Any) -> None: ...
