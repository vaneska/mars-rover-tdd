import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from domains.rover.entities import CommandList, Rover
from domains.rover.use_cases import MoveForecastUseCase
from infra.rover.repositories import RoverPositionFakeRepo, RoverPositionRedisRepo
from rest_framework import status
from rest_framework.views import APIView


class Coffee(APIView):
    @csrf_exempt
    def post(self, requset: HttpRequest):
        return HttpResponse("I'm a teapot", status=status.HTTP_418_IM_A_TEAPOT)


class Commands(APIView):
    @csrf_exempt
    def post(self, request: HttpRequest):

        rover_repo = RoverPositionRedisRepo()
        move_forcast = MoveForecastUseCase(
            rover=Rover(rover_repo.get_current_position())
        )

        position = move_forcast.execute(
            command_list=CommandList(commands=json.loads(request.body).get("command"))
        )

        return JsonResponse({"point": position.dict()}, status=status.HTTP_201_CREATED)
