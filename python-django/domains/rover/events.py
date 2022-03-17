from attrs import define
from domains.rover.entities import Position


class RoverEvent:
    pass


@define
class RoverPositionChanged(RoverEvent):
    position: Position
