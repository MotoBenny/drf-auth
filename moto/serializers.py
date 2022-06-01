from rest_framework import serializers
from .models import Moto


class MotoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'model', 'year', 'engine_size', 'brand')
        model = Moto
