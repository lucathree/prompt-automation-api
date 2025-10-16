from rest_framework import serializers

from django.utils.translation import gettext_lazy as _

from prompto.templates import models, vo


class PromptTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PromptTemplate
        fields = [
            "id",
            "name",
            "description",
            "content",
            "system_prompt",
            "temperature",
            "max_tokens",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def is_valid(self, raise_exception=False):
        content = self.initial_data.get("content", "")
        try:
            vo.ValidatedTemplate(content)
        except ValueError as e:
            if raise_exception:
                raise serializers.ValidationError(detail=_(str(e)), code="invalid")
            return False
        return super().is_valid(raise_exception=raise_exception)


class TemplateValidateSerializer(serializers.Serializer):
    content = serializers.CharField()
