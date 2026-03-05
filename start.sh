#!/bin/bash
# Apply database migrations
python manage.py migrate

# Create a default superuser if it doesn't exist
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
"

# Create a demo product so the homepage isn't empty and doesn't crash
python manage.py shell -c "
from store.models import Category, Product
cat, _ = Category.objects.get_or_create(name='Smartphones', slug='smartphones')
if not Product.objects.exists():
    Product.objects.create(name='Mobile Samsung S26', slug='mobile-samsung-s26', category=cat, description='Latest 5G smartphone from Samsung with incredible camera and battery life.', price=799.99, stock=50, is_available=True)
"

# Start the Gunicorn server
gunicorn ecommerce_project.wsgi:application
