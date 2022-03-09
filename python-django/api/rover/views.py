from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView


class Commands(APIView):

    @csrf_exempt
    def coffee(self):
        return HttpResponse("I'm a teapot", status=status.HTTP_418_IM_A_TEAPOT)

    @csrf_exempt
    def commands(self):
        return JsonResponse({ "point": { "x": 2, "y": 3, "direction": "N" }}, status=status.HTTP_201_CREATED)
