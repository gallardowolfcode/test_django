from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee
from .models import Request

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name']

class PostSerializer(serializers.ModelSerializer):

    user = UserSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ['uuid']

class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        exclude = []