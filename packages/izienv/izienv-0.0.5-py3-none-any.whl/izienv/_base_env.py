from typing import Type, TypeVar, Callable
import os

T_BaseEnv = TypeVar("T_BaseEnv", bound="BaseEnv")

class BaseEnv:
    def __init__(self, *, name: str):
        self._name = name
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def name_upper(self) -> str:
        return self.name.upper()

def load_env_var(*, raise_none_error: bool = True):
    def decorator(func: Callable[[Type[T_BaseEnv]], str]):
        """ Raise error if result is None."""
        def wrapper(self: Type[T_BaseEnv]) -> str:
            env_var = os.getenv(f"{self.name_upper}_{func(self)}")
            if raise_none_error and env_var is None:
                raise ValueError(f"`{func.__name__}` for `{self.name_upper}` is None")
            return env_var
        return wrapper
    return decorator
