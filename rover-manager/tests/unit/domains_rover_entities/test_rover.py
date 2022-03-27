import pytest
from domains.rover.entities import DirectionType, Position, Rover


@pytest.mark.parametrize(
    "position,expected_position",
    [
        (
            Position(x=1, y=1, direction=DirectionType.North),
            Position(x=1, y=1, direction=DirectionType.West),
        ),
        (
            Position(x=1, y=1, direction=DirectionType.West),
            Position(x=1, y=1, direction=DirectionType.South),
        ),
        (
            Position(x=1, y=1, direction=DirectionType.South),
            Position(x=1, y=1, direction=DirectionType.East),
        ),
        (
            Position(x=1, y=1, direction=DirectionType.East),
            Position(x=1, y=1, direction=DirectionType.North),
        ),
    ],
)
def test_rotate_left(position, expected_position):

    rover = Rover(position=position)

    result = rover.rotate_left()

    assert result == expected_position


@pytest.mark.parametrize(
    "position,expected_position",
    [
        (
            Position(x=1, y=1, direction=DirectionType.North),
            Position(x=1, y=1, direction=DirectionType.East),
        ),
        (
            Position(x=1, y=1, direction=DirectionType.East),
            Position(x=1, y=1, direction=DirectionType.South),
        ),
        (
            Position(x=1, y=1, direction=DirectionType.South),
            Position(x=1, y=1, direction=DirectionType.West),
        ),
        (
            Position(x=1, y=1, direction=DirectionType.West),
            Position(x=1, y=1, direction=DirectionType.North),
        ),
    ],
)
def test_rotate_right(position, expected_position):

    rover = Rover(position=position)

    result = rover.rotate_right()

    assert result == expected_position


@pytest.mark.parametrize(
    "position,expected_position",
    [
        (
            Position(x=1, y=1, direction=DirectionType.North),
            Position(x=1, y=2, direction=DirectionType.North),
        ),
        (
            Position(x=1, y=1, direction=DirectionType.West),
            Position(x=0, y=1, direction=DirectionType.West),
        ),
        (
            Position(x=1, y=1, direction=DirectionType.South),
            Position(x=1, y=0, direction=DirectionType.South),
        ),
        (
            Position(x=1, y=1, direction=DirectionType.East),
            Position(x=2, y=1, direction=DirectionType.East),
        ),
    ],
)
def test_move(position, expected_position):

    rover = Rover(position=position)

    result = rover.move()

    assert result == expected_position
