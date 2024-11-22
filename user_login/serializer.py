from rest_framework import serializers
from .models import Data_users

class Data_users_serializer(serializers.ModelSerializer):
    class Meta:
        model = Data_users
        fields = ('name', 'job_position','password')