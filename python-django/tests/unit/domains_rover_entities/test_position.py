from domains.rover.entities import DirectionType, Position


def test_dict():
    position = Position(x=0, y=0, direction=DirectionType.North)

    result = position.dict()

    assert result == {"x": 0, "y": 0, "direction": "N"}
