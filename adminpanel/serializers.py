from rest_framework import serializers
from .models import License


class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = ['user_hwid','expiration_date']
