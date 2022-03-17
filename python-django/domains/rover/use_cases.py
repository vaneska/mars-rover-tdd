import zope.event
from attrs import define
from domains.rover.entities import Command, CommandList, Position, Rover
from domains.rover.events import RoverPositionChanged
from domains.rover.managers import RoverManager
from domains.rover.repositories import RoverPositionRepo


@define
class MoveForecastUseCase:
    rover: Rover

    def execute(self, command_list: CommandList) -> Position:

        for command in command_list.commands:
            if command == Command.MOVE:
                self.rover.move()
            elif command == Command.LEFT:
                self.rover.rotate_left()
            elif command == Command.RIGHT:
                self.rover.rotate_right()

        return self.rover.position


@define
class ProcessCommandsUseCase:
    rover_manager: RoverManager
    position_repo: RoverPositionRepo

    def execute(self, command_list: CommandList) -> None:

        for command in command_list.commands:
            position = self.rover_manager.process_command(command=command)

            if self.position_repo.set_position(position):
                zope.event.notify(RoverPositionChanged(position))
