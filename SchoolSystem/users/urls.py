from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserViewSet, RegisterAPIView

user_router = DefaultRouter()
user_router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(user_router.urls)),
    path("register/", RegisterAPIView.as_view(), name="user-register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    ]
