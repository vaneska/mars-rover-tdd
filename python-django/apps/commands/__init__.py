from domains.rover.entities import CommandList, Rover
from domains.rover.use_cases import MoveForecastUseCase
from flask import Flask, make_response, request
from infra.rover.repositories import RoverPositionRedisRepo


def create_app() -> Flask:

    app = Flask(__name__)

    @app.route("/brew_coffee", methods=["POST"])
    def brew_coffee():
        return make_response("I'm a teapot", 418)

    @app.route("/commands", methods=["POST"])
    def post_commands():

        rover_repo = RoverPositionRedisRepo()
        move_forcast = MoveForecastUseCase(
            rover=Rover(rover_repo.get_current_position())
        )

        position = move_forcast.execute(
            command_list=CommandList.validate(commands_str=request.json.get("command"))
        )

        return make_response({"point": position.dict()}, 201)

    return app


app = create_app()
