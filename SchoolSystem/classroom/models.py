from django.db import models
from base.models import BaseProfileModel
from core.choices import (
    TargetChoices,
    TaskStatusChoices, TestPaperCategoryChoices,
    TestPaperTypeChoices,
    )
from core.models import BaseModel
from users.choices import UserTypeChoices
from users.models import User

class Principal(BaseProfileModel):
    """
    Principal model represents a principal in the school system.

    Example: John Doe, Jane Doe, etc.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="principal", null=True, blank=True
        )


class Student(BaseProfileModel):
    """
    Student model represents a student in the school system.

    Example: John Doe, Jane Doe, etc.
    """

    temp_address = models.TextField(blank=True, null=True)
    enrollment_date = models.DateField()
    classroom = models.ForeignKey(
        "classroom.Classroom", on_delete=models.CASCADE, related_name="students"
        )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student", null=True, blank=True
        )


class Teacher(BaseProfileModel):
    """
    Teacher model represents a teacher in the school system.

    Example: John Doe, Jane Doe, etc.
    """

    hire_date = models.DateField()
    classroom = models.ManyToManyField("classroom.Classroom", related_name="teachers")
    subject = models.ForeignKey(
        "classroom.Subject", on_delete=models.CASCADE, related_name="teachers"
        )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="teacher", null=True, blank=True
        )

class Subject(BaseModel):
    """
    Subject model represents a subject in the school system.

    Example: Mathematics, English, Science, etc.
    """

    name = models.CharField(max_length=100)
    credits = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class Curriculum(BaseModel):
    """
    Curriculum model represents a curriculum in the school system.

    Example: Grade 1, Grade 2, etc.
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    subjects = models.ManyToManyField(Subject, related_name="curriculums")

    def __str__(self):
        return self.name

class Classroom(BaseModel):
    """
    Classroom model represents a classroom in the school system.

    Example: Grade 1 A, Grade 1 B, etc.
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    curriculum = models.ForeignKey(
        Curriculum, on_delete=models.CASCADE, related_name="classroom"
        )

    def __str__(self):
        return self.name

class Assignment(BaseModel):
    """
    Assignment model represents an assignment in the school system.

    Example: Math assignment, English assignment, etc.
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    attachment = models.FileField(upload_to="attachments/assignments/")
    target = models.CharField(
        max_length=50,
        choices=TargetChoices.choices[2:],
        default=TargetChoices.CURRICULUM_SPECIFIC,
        )
    curriculum = models.ForeignKey(
        Curriculum,
        on_delete=models.CASCADE,
        related_name="assignments",
        null=True,
        blank=True,
        )
    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.CASCADE,
        related_name="assignments",
        null=True,
        blank=True,
        )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="assignments"
        )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.target == TargetChoices.CURRICULUM_SPECIFIC and not self.curriculum:
            raise ValueError(
                "Curriculum must be provided for curriculum specific assignments."
                )
        if self.target == TargetChoices.CLASSROOM_SPECIFIC and not self.classroom:
            raise ValueError(
                "Classroom must be provided for classroom specific assignments."
                )

        return super().save(*args, **kwargs)
    
class AssignmentSubmission(BaseModel):
    """
    AssignmentSubmission model represents an assignment submission in the school system.

    Example: Math assignment submission, English assignment submission, etc.
    """

    assignment = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, related_name="submissions"
        )
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="submissions"
        )
    submission_date = models.DateTimeField()
    attachment = models.FileField(upload_to="attachments/assignment_submissions/")
    remarks = models.TextField()

    class Meta:
        unique_together = ["assignment", "student"]

    @property
    def permament_delete(self):
        return True

class Testpaper(BaseModel):
    """
    Testpaper model represents a testpaper in the school system.

    Example: Math testpaper, English testpaper, etc.
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.DurationField()
    total_marks = models.PositiveIntegerField(default=100)
    passing_marks = models.PositiveIntegerField(default=40)
    attachment = models.FileField(upload_to="attachments/testpapers/")
    type = models.CharField(
        max_length=50,
        choices=TestPaperTypeChoices.choices,
        default=TestPaperTypeChoices.TERMINAL,
        )
    category = models.CharField(
        max_length=50,
        choices=TestPaperCategoryChoices.choices,
        default=TestPaperCategoryChoices.THEORY,
        )
    target = models.CharField(
        max_length=50,
        choices=TargetChoices.choices[2:],
        default=TargetChoices.CURRICULUM_SPECIFIC,
        )
    curriculum = models.ForeignKey(
        Curriculum,
        on_delete=models.CASCADE,
        related_name="testpapers",
        null=True,
        blank=True,
        )
    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.CASCADE,
        related_name="testpapers",
        null=True,
        blank=True,
        )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="testpapers"
        )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.target == TargetChoices.CURRICULUM_SPECIFIC and not self.curriculum:
            raise ValueError(
                "Curriculum must be provided for curriculum specific testpapers."
                )
        if self.target == TargetChoices.CLASSROOM_SPECIFIC and not self.classroom:
            raise ValueError(
                "Classroom must be provided for classroom specific testpapers."
                )

        return super().save(*args, **kwargs)

class TestpaperResult(BaseModel):
    """
    TestpaperResult model represents a testpaper result in the school system.

    Example: Math testpaper result, English testpaper result, etc.
    """

    testpaper = models.ForeignKey(
        Testpaper, on_delete=models.CASCADE, related_name="results"
        )
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="results"
        )
    marks = models.PositiveIntegerField()

    class Meta:
        unique_together = ["testpaper", "student"]

    @property
    def permament_delete(self):
        return True

    @property
    def percentage(self):
        return (self.marks / self.testpaper.total_marks) * 100

    @property
    def failed(self):
        return self.marks < self.testpaper.passing_marks
