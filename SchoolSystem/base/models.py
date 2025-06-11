from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from core.models import BaseModel


class BaseProfileModel(models.Model):
    """
    BaseProfileModel model represents a base profile model in the school system.

    Example: John Doe, Jane Doe, etc.
    """

    photo = models.ImageField(upload_to="profiles/")
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    address = models.TextField()
    contact = PhoneNumberField()
    email = models.EmailField()

    @property
    def full_name(self):
        return f"{self.first_name}{f' {self.middle_name}' if self.middle_name else ''} {self.last_name}".strip()

    class Meta:
        abstract = True
