from domains.rover.entities import Rover
from domains.rover.use_cases import MoveForecastUseCase
from domains.shared.entities import CommandList
from flask import Flask, make_response, request
from infra.rover.repositories import (
    CommandListRedisRepo,
    RoverPositionRedisRepo,
)


def create_app() -> Flask:

    app = Flask(__name__)

    @app.route("/brew_coffee", methods=["POST"])
    def brew_coffee():
        return make_response("I'm a teapot", 418)

    @app.route("/commands", methods=["POST"])
    def post_commands():

        rover_repo = RoverPositionRedisRepo()
        commands_list_repo = CommandListRedisRepo()
        move_forcast = MoveForecastUseCase(
            rover=Rover(rover_repo.load_position())
        )

        command_list = CommandList.validate(
            commands_str=request.json.get("command")
        )

        position = move_forcast.execute(command_list=command_list)
        commands_list_repo.push_commands(command_list=command_list)

        return make_response({"point": position.dict()}, 201)

    return app


app = create_app()
