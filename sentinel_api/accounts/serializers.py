from . import models
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'username', 'email', 'phone_number', 'profile_image', 'role']


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = models.User
        fields = ['username', 'email', 'phone_number', 'profile_image', 'role', 'password']

    def create(self, validated_data):
        user = models.User.objects.create_user(
            username=validated_data.get('username', validated_data['email']),
            email=validated_data['email'],
            phone_number=validated_data.get('phone_number'),
            role=validated_data.get('role', 'citizen'),
            password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        try:
            user = models.User.objects.get(email=email)
        except models.User.DoesNotExist:
            raise serializers.ValidationError('Invalid credentials')
        
        # Check if password is correct
        if not user.check_password(password):
            raise serializers.ValidationError('Invalid credentials')
        
        refresh = RefreshToken.for_user(user)
        return {
            "user": {
                "id": user.id,
                "email": user.email,
                "role": user.role,
            },
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }
            
            
            
        