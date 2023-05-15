from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

    def create(self, validated_data):
        return Application.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.applicant = validated_data.get('applicant', instance.applicant)
        instance.education = validated_data.get('education', instance.education)
        instance.age = validated_data.get('age', instance.age)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.message = validated_data.get('message', instance.message)
        instance.opening = validated_data.get('opening', instance.opening)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance