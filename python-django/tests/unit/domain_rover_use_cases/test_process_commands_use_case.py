from domains.rover.entities import Rover
from domains.rover.use_cases import ProcessCommandsUseCase
from domains.shared.entities import (
    Command,
    CommandList,
    DirectionType,
    Position,
)
from infra.rover.managers import MarsRoverManager
from infra.rover.repositories import RoverPositionFakeRepo


def test_success():
    position = Position(x=0, y=0, direction=DirectionType.North)
    position_repo = RoverPositionFakeRepo(position=position)
    use_case = ProcessCommandsUseCase(
        rover_manager=MarsRoverManager(rover=Rover(position=position)),
        position_repo=position_repo,
    )
    use_case.execute(
        command_list=CommandList(
            commands=[Command.MOVE, Command.RIGHT, Command.MOVE, Command.LEFT]
        )
    )

    result = position_repo.get_current_position()

    assert result == Position(x=1, y=1, direction=DirectionType.North)
