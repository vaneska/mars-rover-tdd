from logging import Logger
from typing import Optional

import zope.event
from attrs import define
from domains.rover.entities import Rover
from domains.rover.repositories import (
    CommandListRepo,
    NoCommandsException,
    RoverPositionRepo,
)
from domains.rover.transmiters import RoverGatewayException, RoverTransmitter
from domains.shared.entities import Command, CommandList, Position
from domains.shared.events import (
    ChangingRoverPositionFailed,
    RoverPositionChanged,
    SavingRoverPositionFailed,
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
    commands_list_repo: CommandListRepo
    logger: Logger

    def execute(self) -> None:

        try:
            command_list = self.commands_list_repo.pop_commands()
        except NoCommandsException:
            self.logger.debug("NoCommandsException")
            return

        idx = 0
        for command in command_list.commands:
            try:
                position = self.rover_transmitter.process_command(
                    command=command
                )
            except RoverGatewayException as err:
                event = ChangingRoverPositionFailed(
                    command_list=command_list,
                    current_index=idx,
                    error=str(err),
                )
                zope.event.notify(event)
                self.logger.info(str(event))
                return

            try:
                self.position_repo.save_position(position)
                event = RoverPositionChanged(position)
                self.logger.info(str(event))
                zope.event.notify(event)
            except Exception as err:
                event = SavingRoverPositionFailed(
                    command_list=command_list,
                    current_index=idx,
                    error=str(err),
                )
                zope.event.notify(event)
                self.logger.info(str(event))
                return
            idx += 1
