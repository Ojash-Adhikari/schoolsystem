from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class UserTypeChoices(TextChoices):
    PRINCIPAL = "PRINCIPAL", _("Principal")
    TEACHER = "TEACHER", _("Teacher")
    HR = "HR", _("HR")
    ACCOUNTANT = "ACCOUNTANT", _("Accountant")
    STUDENT = "STUDENT", _("Student")
    PARENT = "PARENT", _("Parent")
