from base.models import BaseProfileModel
from core.serializers import BaseModelSerializer, BaseModelWritableNestedModelSerializer
from rest_framework import serializers
from core.serializers import BaseModelSerializer

class BaseProfileModelSerializer(BaseModelSerializer):
    class Meta:
        model = BaseProfileModel
        fields = (
            "photo",
            "first_name",
            "middle_name",
            "last_name",
            "date_of_birth",
            "address",
            "contact",
            "email",
            )
        extra_kwargs = {
            **BaseModelSerializer.Meta.extra_kwargs,
            }
