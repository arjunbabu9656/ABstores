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

# Create a demo product so the homepage isn't empty and doesn't crash
python manage.py shell -c "
from store.models import Category, Product

cat1, _ = Category.objects.get_or_create(name='Smartphones', slug='smartphones')
cat2, _ = Category.objects.get_or_create(name='Laptops', slug='laptops')
cat3, _ = Category.objects.get_or_create(name='Audio', slug='audio')
cat4, _ = Category.objects.get_or_create(name='Accessories', slug='accessories')

if not Product.objects.exists():
    Product.objects.create(name='Mobile Samsung S26', slug='mobile-samsung-s26', category=cat1, description='Latest 5G smartphone from Samsung with incredible camera and battery life.', price=799.99, stock=50, is_available=True)
    Product.objects.create(name='Apple iPhone 15 Pro', slug='apple-iphone-15-pro', category=cat1, description='The ultimate iPhone experience with A17 Pro chip and titanium design.', price=999.00, stock=30, is_available=True)
    Product.objects.create(name='MacBook Air M3', slug='macbook-air-m3', category=cat2, description='Supercharged by M3. The incredibly thin and light MacBook Air features a liquid retina display.', price=1199.00, stock=20, is_available=True)
    Product.objects.create(name='Sony WH-1000XM5', slug='sony-wh-1000xm5', category=cat3, description='Industry leading noise canceling headphones with Auto NC Optimizer.', price=398.00, stock=100, is_available=True)
    Product.objects.create(name='Apple Watch Series 9', slug='apple-watch-series-9', category=cat4, description='A healthy leap ahead. With double tap, a magical new way to use Apple Watch.', price=399.00, stock=45, is_available=True)
    Product.objects.create(name='Dell XPS 15', slug='dell-xps-15', category=cat2, description='Stunning 15.6 inch OLED display, 13th Gen Intel Core processors, and NVIDIA graphics.', price=1599.99, stock=15, is_available=True)
"

# Start the Gunicorn server
gunicorn ecommerce_project.wsgi:application
