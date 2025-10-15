"""
ASGI config for prompto project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from prompto.settings import AppEnv

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", f"prompto.settings.{AppEnv.current().value}"
)

application = get_asgi_application()
