from django.urls import include, path
from rest_framework.routers import DefaultRouter

from prompto.templates import views

router = DefaultRouter()
router.register(r"templates", views.PromptTemplateViewSet, basename="template")

urlpatterns = [
    path("", include(router.urls)),
]
