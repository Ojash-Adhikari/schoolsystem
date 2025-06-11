from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from core.serializers import BaseModelSerializer
from users.choices import UserTypeChoices, EnrollmentChoices
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = BaseModelSerializer.Meta.fields + ("id", "username", "email", "phone_number", "user_type","is_enrolled")

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    phone_number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "password", "user_type","is_enrolled")

    def create(self, validated_data):
        user_type = validated_data.get("user_type", UserTypeChoices.STUDENT)  # Use STUDENT if not provided
        is_enrolled = validated_data.get("is_enrolled", EnrollmentChoices.PENDING)
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            phone_number=validated_data["phone_number"],
            user_type=user_type,
            password=validated_data["password"],
            is_enrolled =is_enrolled
        )
        return user
