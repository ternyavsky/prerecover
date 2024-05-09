from abc import ABC
from dataclasses import dataclass, field

from src.domain.common.entities.entity import Entity


@dataclass
class AggregateRoot(Entity, ABC):
    _events: list[type] = field(
        default_factory=list, init=False, repr=False, hash=False
    )
