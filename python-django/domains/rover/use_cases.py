from attrs import define
from domains.rover.entities import Command, CommandList, Position, Rover


@define
class MoveForecastUseCase:
    rover: Rover

    def execute(self, command_list: CommandList) -> Position:

        for command in command_list:
            if command == Command.MOVE:
                self.rover.move()
            elif command == Command.LEFT:
                self.rover.rotate_left()
            elif command == Command.RIGHT:
                self.rover.rotate_right()

        return self.rover.position
