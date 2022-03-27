from enum import Enum
from typing import Any, Dict, List

from attrs import define


class Command(Enum):
    MOVE = "M"
    LEFT = "L"
    RIGHT = "R"


@define
class CommandList:
    commands: List[Command]

    @classmethod
    def validate(cls, commands_str: str) -> "CommandList":
        if commands_str is None or not len(commands_str):
            raise ValueError("Empty command string!")

        return cls(commands=[Command(symbol) for symbol in commands_str])

    def __str__(self) -> str:
        return "".join([c.value for c in self.commands])


class DirectionType(Enum):
    North = "N"
    East = "E"
    South = "S"
    West = "W"


@define
class Position:
    x: int
    y: int
    direction: DirectionType

    def dict(self) -> Dict[str, Any]:
        return {
            "x": self.x,
            "y": self.y,
            "direction": self.direction.value,
        }
