from rest_framework import serializers
from .models import Console, Company

class CompanySerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()

    class Meta:
        model = Company
        fields = ['id', 'name']


class ConsoleSerializer(serializers.ModelSerializer):

    company = CompanySerializer(required=False)

    class Meta:
        model = Console
        fields = ['id', 'name', 'short_name', 'year', 'company']

    def validate(self, data):
        if 'company' in data :
            company_id = data['company']['id']
            try :
                Company.objects.get(pk=company_id)
            except Company.DoesNotExist :
                raise serializers.ValidationError('company', 'Company with id %s does not exist' % company_id)
        return data

    def update(self, instance, validated_data):
        company = None
        if 'company' in validated_data :
            company_data = validated_data.pop('company')
            company = Company.objects.get(pk=company_data['id'])

        instance.company = company
        instance.name = validated_data.get('name', instance.name)
        instance.short_name = validated_data.get('short_name', instance.short_name)
        instance.year = validated_data.get('year', instance.year)
        instance.save()
        return instance