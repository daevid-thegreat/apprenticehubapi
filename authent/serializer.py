from rest_framework import serializers
from .models import Userprofile, Company, Apprentice

class NormalUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Userprofile
        fields = ['id', 'name', 'email', 'password']

    def create(self, validated_data):
        user = Userprofile(
            name=validated_data['name'],
            email=validated_data['email'],
            is_master=False
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, validated_data):
        user = Userprofile(
            name=validated_data['name'],
            email=validated_data['email'],
            gender = validated_data['gender'],
            tel = validated_data['tel'],
            company = validated_data['company'],
            is_master=False
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class MasterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Userprofile
        fields = ['id', 'name', 'email', 'password']

    def create(self, validated_data):
        user = Userprofile(
            name=validated_data['name'],
            email=validated_data['email'],
            is_master=True
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, validated_data):
        user = Userprofile(
            name=validated_data['name'],
            email=validated_data['email'],
            gender = validated_data['gender'],
            tel = validated_data['tel'],
            company = validated_data['company'],
            is_master=True
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def add_company (self, validated_data):
        user = Userprofile(
            company = validated_data['company']
        )
        user.save()
        return user
    

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'address', 'tel', 'email', 'website', 'logo']

    def create(self, validated_data):
        company = Company(
            name=validated_data['name'],
            address=validated_data['address'],
            tel=validated_data['tel'],
            email=validated_data['email'],
            website=validated_data['website'],
            logo=validated_data['logo']
        )
        company.save()
        return company
    
    def update(self, validated_data):
        company = Company(
            name=validated_data['name'],
            address=validated_data['address'],
            tel=validated_data['tel'],
            email=validated_data['email'],
            website=validated_data['website'],
            logo=validated_data['logo']
        )
        company.save()
        return company
    


class ApprenticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'address', 'tel', 'email', 'website', 'logo']

    def create(self, validated_data):
        company = Company(
            name=validated_data['name'],
            address=validated_data['address'],
            tel=validated_data['tel'],
            email=validated_data['email'],
            website=validated_data['website'],
            logo=validated_data['logo']
        )
        company.save()
        return company
    
    def update(self, validated_data):
        company = Company(
            name=validated_data['name'],
            address=validated_data['address'],
            tel=validated_data['tel'],
            email=validated_data['email'],
            website=validated_data['website'],
            logo=validated_data['logo']
        )
        company.save()
        return company
