from rest_framework import generics, permissions
from rest_framework.viewsets import ModelViewSet
from users.models import User
from users.serializers import UserSerializer, RegisterSerializer

from django.contrib.auth import get_user_model

User = get_user_model()

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]