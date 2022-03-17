from attrs import define
from domains.shared.entities import CommandList, Position


class RoverEvent:
    pass


@define
class RoverPositionChanged(RoverEvent):
    position: Position


@define
class ChangingRoverPositionFailed(RoverEvent):
    command_list: CommandList
    current_index: int
    error_message: str
