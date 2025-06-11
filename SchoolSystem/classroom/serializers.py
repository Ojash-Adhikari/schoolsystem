from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from base.models import BaseProfileModel
from base.serializers import  BaseProfileModelSerializer
from classroom.models import *
from users.serializers import UserSerializer
from core.serializers import BaseModelSerializer
class PrincipalSerializer(BaseProfileModelSerializer):
    class Meta:
        model = Principal
        fields = BaseProfileModelSerializer.Meta.fields + ("user",)
        extra_kwargs = { **BaseProfileModelSerializer.Meta.extra_kwargs }


class StudentSerializer(BaseProfileModelSerializer):
    class Meta:
        model = Student
        fields = BaseProfileModelSerializer.Meta.fields + (
            "temp_address",
            "enrollment_date",
            "classroom",
            "user",
            )
        extra_kwargs = { **BaseProfileModelSerializer.Meta.extra_kwargs }


class TeacherSerializer(BaseProfileModelSerializer):
    class Meta:
        model = Teacher
        fields = BaseProfileModelSerializer.Meta.fields + (
            "hire_date",
            "classroom",
            "subject",
            "user",
            )
        extra_kwargs = { **BaseProfileModelSerializer.Meta.extra_kwargs }

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user_data = UserSerializer(self.user, context=self.context).data
        try:
            profile = getattr(self.user, 'profile', None)
            if isinstance(profile, Principal):
                user_data["profile"] = PrincipalSerializer(profile, context=self.context).data
            elif isinstance(profile, Student):
                user_data["profile"] = StudentSerializer(profile, context=self.context).data
            elif isinstance(profile, Teacher):
                user_data["profile"] = TeacherSerializer(profile, context=self.context).data
        except BaseProfileModel.DoesNotExist:
            pass
        data["user"] = user_data
        return data

class SubjectSerializer(BaseModelSerializer):
    class Meta:
        model = Subject
        fields = BaseModelSerializer.Meta.fields + (
            "name",
            "credits",
            )
        extra_kwargs = { **BaseModelSerializer.Meta.extra_kwargs }


class CurriculumSerializer(BaseModelSerializer):
    class Meta:
        model = Curriculum
        fields = BaseModelSerializer.Meta.fields + (
            "name",
            "description",
            "start_date",
            "end_date",
            "subjects",
            )
        extra_kwargs = { **BaseModelSerializer.Meta.extra_kwargs }


class classroomerializer(BaseModelSerializer):
    curriculum_data = CurriculumSerializer(read_only=True, source="curriculum")

    class Meta:
        model = Classroom
        fields = BaseModelSerializer.Meta.fields + (
            "name",
            "description",
            "curriculum",
            "curriculum_data",
            )
        extra_kwargs = { **BaseModelSerializer.Meta.extra_kwargs }

class AssignmentSerializer(BaseModelSerializer):
    class Meta:
        model = Assignment
        fields = BaseModelSerializer.Meta.fields + (
            "title",
            "description",
            "attachment",
            "deadline",
            "target",
            "classroom",
            "subject",
            "curriculum",
            )
        extra_kwargs = { **BaseModelSerializer.Meta.extra_kwargs }


class AssignmentSubmissionSerializer(BaseModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = BaseModelSerializer.Meta.fields + (
            "assignment",
            "student",
            "submission_date",
            "attachment",
            "remarks",
            )
        extra_kwargs = { **BaseModelSerializer.Meta.extra_kwargs }
