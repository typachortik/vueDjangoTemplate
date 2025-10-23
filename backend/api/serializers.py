from rest_framework import serializers
from .models import DataRecord

class DataRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRecord
        fields = ['position', 'percent', 'year', 'days']