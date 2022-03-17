from domains.shared.entities import DirectionType, Position


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
