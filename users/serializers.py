from dataclasses import fields
from xml.parsers.expat import model
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ("id", "email", "first_name", "last_name", "date_joined", "password")

        extra_kwargs = {'password': {'write_only': True}}
        