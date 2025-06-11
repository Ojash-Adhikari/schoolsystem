from SchoolSystem.settings import AUTH_USER_MODEL
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    RegexValidator,
    )
from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def all_objects(self):
        return super().get_queryset()

    def deleted(self):
        return super().get_queryset().filter(is_deleted=True)

    def get_all_objects(self):
        return super().get_queryset()

    def get_deleted_objects(self):
        return super().get_queryset().filter(is_deleted=True)

    def get_object(self, pk):
        return super().get_queryset().get(pk=pk)

    def get_object_or_none(self, pk):
        try:
            return super().get_queryset().get(pk=pk)
        except self.model.DoesNotExist:
            return None

class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    created_by = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="created_%(app_label)s_%(class)s",
        null=True,
        blank=True,
        )
    updated_by = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="updated_%(app_label)s_%(class)s",
        null=True,
        blank=True,
        )
    deleted_by = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="deleted_%(app_label)s_%(class)s",
        null=True,
        blank=True,
        )

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = BaseManager()

    class Meta:
        abstract = True

    @property
    def permanent_delete(self):
        return False

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.permanent_delete:
            return self.hard_delete(*args, **kwargs)

        return self.soft_delete(*args, **kwargs)

    def undelete(self, *args, **kwargs):
        self.deleted_at = None
        self.is_deleted = False
        super().save(*args, **kwargs)

    def soft_delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        super().save(*args, **kwargs)

    def hard_delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)


