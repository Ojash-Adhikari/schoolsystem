from django.urls import include, path
from rest_framework.routers import DefaultRouter

from classroom.views import *
app_name = "classroom"

classroom_router = DefaultRouter()

classroom_router.register(r"subjects", SubjectViewSet)
classroom_router.register(r"curriculums", CurriculumViewSet)
classroom_router.register(r"classroom", ClassroomViewSet)
classroom_router.register(r"assignments", AssignmentViewSet)
classroom_router.register(r"assignment-submissions", AssignmentSubmissionViewSet)
classroom_router.register(r"principals", PrincipalViewSet)
classroom_router.register(r"teachers", TeacherViewSet)
classroom_router.register(r"students", StudentViewSet)

urlpatterns = [
    path("", include(classroom_router.urls)),
    ]
