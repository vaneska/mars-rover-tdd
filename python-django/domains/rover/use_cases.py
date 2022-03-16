from attrs import define
from domains.rover.entities import Command, CommandList, Position, Rover
from domains.rover.gateways import RoverGateway
from domains.rover.repositories import RoverPositionRepo


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


@define
class ProcessCommandsUseCase:
    rover_gateway: RoverGateway
    position_repo: RoverPositionRepo

    def execute(self, command_list: CommandList) -> None:

        for command in command_list:
            position = self.rover_gateway.process_command(command=command)
            self.position_repo.set_position(position=position)
