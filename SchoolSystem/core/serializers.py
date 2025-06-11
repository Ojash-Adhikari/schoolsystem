
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers
from rest_framework.request import Request

from core.models import BaseModel


class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = (
            "id",
            "is_deleted",
            "created_by",
            "updated_by",
            "deleted_by",
            "created_at",
            "updated_at",
            "deleted_at",
        )

        extra_kwargs = {
            "is_deleted": {"read_only": True},
            "created_by": {"read_only": True},
            "updated_by": {"read_only": True},
            "deleted_by": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            "deleted_at": {"read_only": True},
        }

    @property
    def request(self) -> Request:
        return self.context.get("request")

    def save(self, **kwargs):
        manipulation_data = {}
        if self.request:
            if not self.instance:
                manipulation_data["created_by"] = self.request.user
            manipulation_data["updated_by"] = self.request.user
        return super().save(**{**kwargs, **manipulation_data})


class BaseModelWritableNestedModelSerializer(
    WritableNestedModelSerializer, BaseModelSerializer
):
    pass
