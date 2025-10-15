"""
WSGI config for prompto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from prompto.settings import AppEnv

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", f"prompto.settings.{AppEnv.current().value}"
)

application = get_wsgi_application()
