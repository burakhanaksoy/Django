from rest_framework import serializers
from .models import Person, Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'country', 'net_worth_usd']


class PersonSerializer(serializers.ModelSerializer):
    company = serializers.CharField()

    class Meta:
        model = Person
        fields = ['name', 'age', 'gender', 'company']

    def create(self, validated_data):
        company_name = validated_data.pop('company', None)
        company_qs = Company.objects.filter(name__iexact=company_name)
        person = super().create(validated_data)
        person.company = company_qs[0]
        person.save()
        return person
