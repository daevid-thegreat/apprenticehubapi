from rest_framework import serializers
from .models import Opening


class OpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opening
        fields = ['id', 'headline', 'description', 'pay', 'level', 'job_type', 'requirements', 'created_at', 'updated_at']

