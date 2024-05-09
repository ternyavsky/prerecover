from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ApiConfig:
    host: str
    port: int
    debug: bool = __debug__


@dataclass
class Config:
    api: ApiConfig
    # db: Optional[type]
    # logging: Optional[type]
    # event_bus: Optional[type]