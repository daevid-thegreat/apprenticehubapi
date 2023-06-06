from rest_framework import serializers
from .models import Opening, Application


class OpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opening
        fields = ['id', 'uid', 'headline', 'description', 'pay', 'level', 'job_type', 'created_at']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'opening', 'user', 'created_at', 'email', 'education', 'age', 'tel', 'message', 'status')
