from rest_framework.viewsets import ModelViewSet

from classroom.models import *
from classroom.serializers import *


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CurriculumViewSet(ModelViewSet):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer


class ClassroomViewSet(ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = classroomerializer

class AssignmentViewSet(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class AssignmentSubmissionViewSet(ModelViewSet):
    queryset = AssignmentSubmission.objects.all()
    serializer_class = AssignmentSubmissionSerializer

class PrincipalViewSet(ModelViewSet):
    queryset = Principal.objects.all()
    serializer_class = PrincipalSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

