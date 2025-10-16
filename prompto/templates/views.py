from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from prompto.templates import models, serializers, vo


class PromptTemplateViewSet(viewsets.ModelViewSet):
    queryset = models.PromptTemplate.objects.all()
    serializer_class = serializers.PromptTemplateSerializer

    @action(detail=False, methods=["post"])
    def validate(self, request: Request):
        serializer = serializers.TemplateValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        content = serializer.validated_data["content"]
        try:
            validated_template = vo.ValidatedTemplate(content)
        except ValueError as e:
            return Response(
                {"is_valid": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {
                "is_valid": True,
                "variables": validated_template.get_identifiers(),
            }
        )

    @action(detail=True, methods=["get"])
    def variables(self, request: Request, pk: int = None):
        template = self.get_object()
        validated_template = vo.ValidatedTemplate(template.content)
        return Response({"variables": validated_template.get_identifiers()})
