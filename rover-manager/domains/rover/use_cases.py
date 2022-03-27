import zope.event
from attrs import define
from domains.rover.entities import Rover
from domains.rover.transmiters import RoverGatewayException, RoverTransmitter
from domains.rover.repositories import RoverPositionRepo
from domains.shared.entities import Command, CommandList, Position
from domains.shared.events import (
    ChangingRoverPositionFailed,
    RoverPositionChanged,
)


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
    rover_transmitter: RoverTransmitter
    position_repo: RoverPositionRepo

    def execute(self, command_list: CommandList) -> None:

        idx = 0
        for command in command_list.commands:
            try:
                position = self.rover_transmitter.process_command(
                    command=command
                )
            except RoverGatewayException as err:
                zope.event.notify(
                    ChangingRoverPositionFailed(
                        command_list=command_list,
                        current_index=idx,
                        error_message=str(err),
                    )
                )
                return

            try:
                self.position_repo.set_position(position)
                zope.event.notify(RoverPositionChanged(position))
            except Exception as err:
                zope.event.notify(
                    ChangingRoverPositionFailed(
                        command_list=command_list,
                        current_index=idx,
                        error_message=str(err),
                    )
                )
                return
            idx += 1
