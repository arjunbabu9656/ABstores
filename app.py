# Render default start command is `gunicorn app:app`.
# This file bridges that default command to the Django application so the user
# doesn't have to manually configure the start command in the Render dashboard.

from ecommerce_project.wsgi import application as app
