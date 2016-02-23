from . import models
from rest_framework import serializers


class JokeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Joke
        fields = ('text', 'funny', 'user')


class VoteUpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.VoteUp
        fields = ('joke', 'user')


class LongModelNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ExtendedGroupDescriptionForExampleHowToUseRestApi
        fields = ('description', 'name', 'id', 'url')
