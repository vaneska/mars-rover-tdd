import logging
from cmath import log

from domains.rover.entities import Rover
from domains.rover.use_cases import ProcessCommandsUseCase
from domains.shared.entities import (
    Command,
    CommandList,
    DirectionType,
    Position,
)
from infra.rover.repositories import CommandListFakeRepo, RoverPositionFakeRepo
from infra.rover.transmitters import MarsRoverTransmitter


def test_success():
    position = Position(x=0, y=0, direction=DirectionType.North)
    position_repo = RoverPositionFakeRepo(position=position)
    command_list_repo = CommandListFakeRepo()
    use_case = ProcessCommandsUseCase(
        rover_transmitter=MarsRoverTransmitter(rover=Rover(position=position)),
        position_repo=position_repo,
        commands_list_repo=command_list_repo,
        logger=logging.getLogger(),
    )
    command_list_repo.push_commands(CommandList(commands=[Command.MOVE]))
    use_case.execute()

    result = position_repo.load_position()

    assert result == Position(x=0, y=1, direction=DirectionType.North)
