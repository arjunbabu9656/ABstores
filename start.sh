#!/bin/bash
# Apply database migrations
python manage.py migrate

# Create a default superuser if it doesn't exist, and force reset password to admin123
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
else:
    u = User.objects.get(username='admin')
    u.set_password('admin123')
    u.save()
"

# Run the Database Sync (Python-as-the-Brain Controller)
python seed_db.py


# Start the Gunicorn server
gunicorn ecommerce_project.wsgi:application
