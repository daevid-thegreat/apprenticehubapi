from rest_framework import serializers
from .models import Opening


class OpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opening
        fields = ['id', 'title', 'description', 'company', 'location', 'salary', 'experience', 'skills', 'is_active',  'created_at', 'updated_at']

    def create(self, validated_data):
        opening = Opening(
            title=validated_data['title'],
            description=validated_data['description'],
            company=validated_data['company'],
            location=validated_data['location'],
            salary=validated_data['salary'],
            experience=validated_data['experience'],
            skills=validated_data['skills'],
            is_active=validated_data['is_active'],
            is_filled=validated_data['is_filled'],
        )
        opening.save()
        return opening

    def update(self, validated_data):
        opening = Opening(
            title=validated_data['title'],
            description=validated_data['description'],
            company=validated_data['company'],
            location=validated_data['location'],
            salary=validated_data['salary'],
            experience=validated_data['experience'],
            skills=validated_data['skills'],
            is_active=validated_data['is_active'],
            is_filled=validated_data['is_filled'],
        )
        opening.save()
        return opening