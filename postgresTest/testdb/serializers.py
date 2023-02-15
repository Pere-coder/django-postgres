from rest_framework import serializers
from testdb.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'email', 'date_of_birth', 'country_of_birth','gender']
    