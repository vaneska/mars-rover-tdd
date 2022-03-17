from enum import Enum
from typing import Any, Dict, Iterable, Iterator, List

from attrs import define


class DirectionType(Enum):
    North = "N"
    East = "E"
    South = "S"
    West = "W"


class Command(Enum):
    MOVE = "M"
    LEFT = "L"
    RIGHT = "R"


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


class Rover:
    def __init__(self, position: Position) -> None:
        self.position = position

    def move(self) -> Position:
        if self.position.direction == DirectionType.North:
            self.position.y += 1

        elif self.position.direction == DirectionType.East:
            self.position.x += 1

        elif self.position.direction == DirectionType.South:
            self.position.y -= 1

        elif self.position.direction == DirectionType.West:
            self.position.x -= 1

        return self.position

    def rotate_left(self) -> Position:
        next_direction = {
            DirectionType.North: DirectionType.West,
            DirectionType.West: DirectionType.South,
            DirectionType.South: DirectionType.East,
            DirectionType.East: DirectionType.North,
        }
        self.position.direction = next_direction[self.position.direction]

        return self.position

    def rotate_right(self) -> Position:
        next_direction = {
            DirectionType.North: DirectionType.East,
            DirectionType.East: DirectionType.South,
            DirectionType.South: DirectionType.West,
            DirectionType.West: DirectionType.North,
        }
        self.position.direction = next_direction[self.position.direction]

        return self.position


@define
class CommandList:
    commands: List[Command]

    @classmethod
    def validate(cls, commands_str: str) -> "CommandList":
        if commands_str is None or not len(commands_str):
            raise ValueError("Empty command string!")

        return cls(commands=[Command(symbol) for symbol in commands_str])
