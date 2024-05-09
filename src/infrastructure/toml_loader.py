import os
import tomllib
from typing import Optional, TypeVar

from adaptix import Retort

T = TypeVar("T")
DEFAULT_CONFIG_PATH = "./config/dev.toml"


def toml_read(path: str) -> dict:
    with open(path, "rb") as f:
        return tomllib.load(f)


def load_config(
    config_type: type[T], config_scope: Optional[str] = None, path: Optional[str] = None
) -> T:
    if path is None:
        path = os.getenv("CONFIG_PATH", DEFAULT_CONFIG_PATH)

    data = toml_read(path)

    if config_scope is not None:
        data = data[config_scope]

    dcf = Retort()
    config = dcf.load(data, config_type)
    return config
