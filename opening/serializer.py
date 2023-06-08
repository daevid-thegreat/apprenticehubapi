from rest_framework import serializers
from .models import Opening, Application


class OpeningSerializer(serializers.ModelSerializer):

    headline = serializers.CharField(max_length=50, required=False)
    description = serializers.CharField(max_length=400, required=False)
    pay = serializers.CharField(max_length=50, required=False)
    level = serializers.CharField(max_length=50, required=False)
    job_type = serializers.CharField(max_length=50, required=False)
    class Meta:
        model = Opening
        fields = ['id', 'uid', 'headline', 'description', 'pay', 'level', 'job_type', 'created_at']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'opening', 'user', 'created_at', 'email', 'education', 'age', 'tel', 'message', 'status')
