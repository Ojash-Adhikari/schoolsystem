from rest_framework import generics, permissions
from rest_framework.viewsets import ModelViewSet
from users.models import User
from users.serializers import UserSerializer, RegisterSerializer
from .permissions import CanViewUsers
from rest_framework.permissions import IsAuthenticated

from users.choices import UserTypeChoices
from django.contrib.auth import get_user_model

User = get_user_model()

class UserViewSet(ModelViewSet):
    queryset = User.objects.none()  
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, CanViewUsers]

    def get_queryset(self):
        user = self.request.user

        if user.user_type == UserTypeChoices.PRINCIPAL:
            return User.objects.all()

        elif user.user_type == UserTypeChoices.TEACHER:
            return User.objects.filter(user_type=UserTypeChoices.STUDENT, created_by=user)

        elif user.user_type == UserTypeChoices.STUDENT:
            return User.objects.filter(id=user.id)

        return User.objects.none()

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]