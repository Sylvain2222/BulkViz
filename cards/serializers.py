from rest_framework import serializers
from cards.models import Element


class CardSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
