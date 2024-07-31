from typing import Type, TypeVar, Callable
from pathlib import Path
import os

from izienv._load_izienv import load_izienv

T_BaseEnv = TypeVar("T_BaseEnv", bound="BaseEnv")

class BaseEnv:
    def __init__(self, *, name: str, path_envs: Path = Path(".envs"), override: bool = True):
        self.name = name
        self.path_envs = path_envs
        load_izienv(name=name, path_envs=self.path_envs, override=override)
    
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

