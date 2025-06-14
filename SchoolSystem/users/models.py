from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from core.models import BaseModel
from users.choices import UserTypeChoices, EnrollmentChoices
# Create your models here.
class User(BaseModel, AbstractUser):
    user_type = models.CharField(
        max_length=20,
        choices=UserTypeChoices.choices,
        default=UserTypeChoices.STUDENT,
        )
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(unique=True)
    is_enrolled = models.CharField(
        max_length=20,
        choices=EnrollmentChoices.choices,
        default=EnrollmentChoices.PENDING
    )

    @property
    def profile(self):
        if self.user_type == UserTypeChoices.STUDENT:
            return self.student
        elif self.user_type == UserTypeChoices.TEACHER:
            return self.teacher
        elif self.user_type == UserTypeChoices.PRINCIPAL:
            return self.principal
        return None