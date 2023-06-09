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
    name = serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model = Userprofile
        fields = ['name']  # Include other fields as needed


class OgSerializer(serializers.ModelSerializer):
    headline = serializers.CharField(source='opening.headline', read_only=True)

    class Meta:
        model = Opening
        fields = ['headline']  # Include other fields as needed


class ApplicationSerializer(serializers.ModelSerializer):
    opening = OgSerializer()
    user = UserprofileSerializer()

    class Meta:
        model = Application
        fields = ['id', 'opening', 'user', 'created_at', 'email', 'education', 'age', 'tel', 'message', 'status']


class ApprenticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apprentice
        fields = ('id', 'uid', 'first_name', 'last_name', 'email', 'created_at', 'pay')
