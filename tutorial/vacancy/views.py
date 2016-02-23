from .import models
from rest_framework import viewsets
from . import serializers


class FunnyJokesViewSet(viewsets.ModelViewSet):
    queryset = models.Joke.objects.filter(funny=True)
    serializer_class = serializers.JokeSerializer


class VoteUpViewSet(viewsets.ModelViewSet):
    queryset = models.VoteUp.objects.all()
    serializer_class = serializers.VoteUpSerializer

class DescriptionViewSet(viewsets.ModelViewSet):
    queryset = models.ExtendedGroupDescriptionForExampleHowToUseRestApi.objects.all()
    serializer_class = serializers.LongModelNameSerializer