import pytest
from domains.rover.entities import Rover
from domains.shared.entities import Command, DirectionType, Position
from infra.rover.transmitters import MarsRoverTransmitter


@pytest.mark.parametrize(
    "command,expected_position",
    [
        (Command.MOVE, Position(x=0, y=1, direction=DirectionType.North)),
        (Command.LEFT, Position(x=0, y=0, direction=DirectionType.West)),
        (Command.RIGHT, Position(x=0, y=0, direction=DirectionType.East)),
    ],
)
def test_successful_processed_command(command, expected_position):

    manager = MarsRoverTransmitter(
        rover=Rover(Position(x=0, y=0, direction=DirectionType.North))
    )

    position = manager.process_command(command)

    assert position == expected_position
