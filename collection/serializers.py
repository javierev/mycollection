from rest_framework import serializers
from .models import Console

class ConsoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Console
        fields = ['pk', 'name', 'short_name', 'year']