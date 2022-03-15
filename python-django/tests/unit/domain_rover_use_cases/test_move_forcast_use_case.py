from domains.rover.entities import Command, CommandList, DirectionType, Position, Rover
from domains.rover.use_cases import MoveForecastUseCase


def test_success():
    use_case = MoveForecastUseCase(
        rover=Rover(Position(x=0, y=0, direction=DirectionType.North))
    )
    result = use_case.execute(
        command_list=CommandList(
            commands=[Command.MOVE, Command.RIGHT, Command.MOVE, Command.LEFT]
        )
    )

    assert result == Position(x=1, y=1, direction=DirectionType.North)
