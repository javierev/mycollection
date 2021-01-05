from rest_framework import serializers
from .models import Console

class ConsoleSerializer(serializers.ModelSerializer):

    id = serializers.SerializerMethodField('get_pk')

    class Meta:
        model = Console
        fields = ['id', 'name', 'short_name', 'year']

    def get_pk(self, obj):
        return obj.pk

class ConsoleUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Console
        fields = ['name', 'short_name', 'year']