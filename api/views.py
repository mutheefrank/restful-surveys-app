# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from client.models import *
from rest_framework import viewsets
from serializers import DrinkSurveySerializer, DrinkSerializer,LocationSerializer

from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

@api_view(["POST"])
def login(request):
    """
    token authentication view
    """
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})


class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = (IsAuthenticated,)


class LocationViewSet(viewsets.ModelViewSet):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticated,)

class DrinkSurveyViewSet(viewsets.ModelViewSet):

    queryset = DrinkSurvey.objects.all()
    serializer_class = DrinkSurveySerializer
    permission_classes = (IsAuthenticated,)

