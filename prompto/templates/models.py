from django.db import models


class PromptTemplate(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(
        help_text="'$' 구분자를 사용하여 작성 (예: Hello, $name!)"
    )
    system_prompt = models.TextField(
        blank=True, null=True, help_text="시스템 프롬프트 (선택사항)"
    )
    temperature = models.FloatField(blank=True, null=True)
    max_tokens = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
