from rest_framework import serializers
from .models import Console, Company

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id', 'name']


class ConsoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Console
        fields = ['id', 'name', 'short_name', 'year', 'company']