from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserRegisterationSerializer(serializers.ModelSerializer):
    """ A serializer for user registeration."""
    email2 = serializers.EmailField(label='Confirm Email', write_only=True)
    password2 = serializers.CharField(label='Confirm Password', 
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'email2', 
            'password', 'password2']
        extra_kwargs = {"password": {'write_only': True}}

    def validate_password(self, value):
        """Validate that password meet django auth validators."""
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError({'password':e})
        return value      

    def validate(self, data):
        """
        Validate that the username is unique.
        Validate that the two emails match and unique.
        Validate that the two passwords match.
        """
        # check if the username has already been used.
        username = data.get('username')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username':"An account with this Username already exists."})    
        # check if the two emails match.
        email1 = data.get('email')
        email2 = data.get('email2')
        if email1 != email2:
            raise serializers.ValidationError({'email':'The two Emails must match.'})
        # check if the email has already been used.
        if User.objects.filter(email=email1).exists():
            raise serializers.ValidationError({'email':"An account with this Email already exists."})
        # check if the two passwords match.
        password1 = data.get('password')
        password2 = data.get('password2')
        if password1 != password2:
            raise serializers.ValidationError({'password':'The two Passwords must match.'})
        return data

    def create(self, validated_data):
        """Create new user."""
        email2 = validated_data.pop('email2')
        password2 = validated_data.pop('password2')   
        user_obj = User.objects.create_user(**validated_data)         
        return user_obj


class UserLoginSerializer(serializers.ModelSerializer):
    """A serializer for user login."""
    username = serializers.CharField()
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'token']
        extra_kwargs = {"password": {'write_only': True}}

    def get_token(self, obj):
        user = User.objects.get(username=obj['username'])
        refresh = RefreshToken.for_user(user)
        response = {'refresh': str(refresh), 'access': str(
            refresh.access_token), }
        return response

    def validate(self, data):
        """Validate entered data."""
        username = data.get("username", None)
        password = data["password"]
        # check if the entered username and password are correct.
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        return data