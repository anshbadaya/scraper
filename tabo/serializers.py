from rest_framework import serializers
from .models import Processed

class ProcessedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processed
        fields = ('temperature', 'time')
