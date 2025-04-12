from api.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, Services, UsedList
from django.contrib.auth import get_user_model



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 

    def create(self, validated_data):
        # Extract password from the validated data
        password = validated_data.pop('password', None)

        # Create the user instance without the password
        user = User(**validated_data)

        # If password is provided, set it (this will hash it)
        if password:
            user.set_password(password)
        user.save()
        
        return user

    def update(self, instance, validated_data):
        # Extract password from the validated data
        password = validated_data.pop('password', None)

        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # If password is provided, set it (this will hash it)
        if password:
            instance.set_password(password)
        
        # Save the updated instance
        instance.save()
        
        return instance


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Get the token data from the parent class
        data = super().validate(attrs)

        # Get the token object
        token = self.get_token(self.user)

        # Add custom claims to the token
        token['username'] = self.user.username  # Adding a custom claim to the token
        
        # Update the response data with the tokens
        data['access'] = str(token.access_token)
        data['refresh'] = str(token)

        return data


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'



class UsedListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsedList
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # These are claims, you can add custom claims
        token['username'] = user.username
        token['email'] = user.email
        return token

