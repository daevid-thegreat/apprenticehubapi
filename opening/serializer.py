from rest_framework import serializers
from .models import Opening, Application, Apprentice
from authent.models import Userprofile


class OpeningSerializer(serializers.ModelSerializer):
    headline = serializers.CharField(max_length=50, required=False)
    description = serializers.CharField(max_length=400, required=False)
    pay = serializers.CharField(max_length=50, required=False)
    level = serializers.CharField(max_length=50, required=False)
    job_type = serializers.CharField(max_length=50, required=False)

    class Meta:
        model = Opening
        fields = ['id', 'uid', 'headline', 'description', 'pay', 'level', 'job_type', 'created_at']


class UserprofileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='name', read_only=True)

    class Meta:
        model = Userprofile
        fields = ['name']


class OgSerializer(serializers.ModelSerializer):
    headline = serializers.CharField(source='opening.headline', read_only=True)

    class Meta:
        model = Opening
        fields = ['headline']


class ApplicationSerializer(serializers.ModelSerializer):
    user = UserprofileSerializer()
    opening = OgSerializer()
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Application
        fields = ['id', 'user', 'opening', 'created_at', 'email', 'education', 'age', 'tel', 'message', 'status']


class ApprenticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apprentice
        fields = ('id', 'uid', 'first_name', 'last_name', 'email', 'created_at', 'pay')
