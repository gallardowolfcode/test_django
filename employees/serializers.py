from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = []
