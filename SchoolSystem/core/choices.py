from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class TestPaperCategoryChoices(TextChoices):
    THEORY = "theory", _("Theory")
    PRACTICAL = "practical", _("Practical")


class TestPaperTypeChoices(TextChoices):
    PRACTICE = "practice", _("Practice")
    MOCK = "mock", _("Mock")
    UNIT = "unit", _("Unit")
    TERMINAL = "terminal", _("Terminal")


class TaskStatusChoices(TextChoices):
    PENDING = "pending", _("Pending")
    IN_PROGRESS = "in_progress", _("In Progress")
    COMPLETED = "completed", _("Completed")
    CANCELLED = "cancelled", _("Cancelled")

class TargetChoices(TextChoices):
    ORGANIZATION_SPECIFIC = "ORGANIZATION_SPECIFIC", _("Organization Specific")
    ROLE_SPECIFIC = "ROLE_SPECIFIC", _("Role Specific")
    CURRICULUM_SPECIFIC = "CURRICULUM_SPECIFIC", _("Curriculum Specific")
    CLASSROOM_SPECIFIC = "CLASSROOM_SPECIFIC", _("Classroom Specific")
    SUBJECT_SPECIFIC = "SUBJECT_SPECIFIC", _("Subject Specific")

