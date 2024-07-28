from functools import wraps
from typing import Dict, Any, Callable

from executor._executor import SubProcessExecutor
from executor._result import Result


def executor[**P, R](env: Dict[str, Any] | None = None) -> Callable[[Callable[P, R]], Callable[P, Result | None]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Result | None:
            result = SubProcessExecutor(args=func(*args, **kwargs), env=env).executor()
            return result

        return wrapper

    return decorator
