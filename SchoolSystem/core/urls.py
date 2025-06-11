from django.urls import include, path
from rest_framework.routers import DefaultRouter



app_name = "core"


urlpatterns = [
    path("classroom/", include("classroom.urls")),
    path("users/", include("users.urls")),
    ]
