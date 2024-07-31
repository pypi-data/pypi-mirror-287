from pathlib import Path
from dotenv import load_dotenv

def __path_env(path_envs: Path, name: str) -> Path:
    return path_envs / f".env_{name}"

def __load_env_base(path_envs: Path, override: bool = True) -> None:
    path_base = __path_env(path_envs=path_envs, name="base")
    if path_base.exists():
        load_dotenv(path_base, override=override)


def load_izienv(path_envs: Path, name: str, override: bool = True) -> None:
    # Load .env_base if exists.
    __load_env_base(path_envs=path_envs, override=override)

    # Load .env_{name}.
    path_env = __path_env(path_envs=path_envs, name=name)
    load_dotenv(path_env, override=override)
