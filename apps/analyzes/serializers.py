from rest_framework import serializers

from .models import Analyze

class AnalyzeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analyze
        fields = '__all__'