import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from store.models import Category, Product

def seed_data():
    print("🚀 Starting Database Sync...")

    # 1. Define Categories
    # We use slugs as the unique identifier for syncing
    categories_data = [
        {'name': 'Men', 'slug': 'men'},
        {'name': 'Essentials', 'slug': 'essentials'},
        {'name': 'Smartphones', 'slug': 'smartphones'},
        {'name': 'Laptops', 'slug': 'laptops'},
    ]

    category_map = {}
    for cat_data in categories_data:
        cat, created = Category.objects.update_or_create(
            slug=cat_data['slug'].lower(),
            defaults={'name': cat_data['name']}
        )
        category_map[cat_data['slug']] = cat
        status = "Created" if created else "Updated"
        print(f"📁 Category: {cat.name} ({status})")

    # 2. Define Products
    # We use slugs as the unique identifier for syncing
    products_data = [
        {
            'name': 'Men OverTshirt',
            'slug': 'men-over-tshirt',
            'price': 4500.00,
            'category_slug': 'men',
            'description': 'Premium heavy-weight oversized tshirt for a modern fit.',
            'stock': 100
        },
        {
            'name': 'Structured Technical Blazer',
            'slug': 'structured-technical-blazer',
            'price': 2200.00,
            'category_slug': 'men',
            'description': 'A versatile blazer with technical fabric and modern silhouette.',
            'stock': 50
        },
        {
            'name': 'Men Technical Jacket',
            'slug': 'men-technical-jacket',
            'price': 3500.00,
            'category_slug': 'essentials',
            'description': 'All-weather technical jacket from our essentials line.',
            'stock': 30
        },
        {
            'name': 'Mobile Samsung S26',
            'slug': 'mobile-samsung-s26',
            'price': 799.99,
            'category_slug': 'smartphones',
            'description': 'Latest 5G smartphone from Samsung with incredible camera and battery life.',
            'stock': 50
        }
    ]

    for p_data in products_data:
        # Get the category object
        category = category_map.get(p_data['category_slug'])
        
        if category is not None:
            product, created = Product.objects.update_or_create(
                slug=str(p_data['slug']).lower(),
                defaults={
                    'name': p_data['name'],
                    'price': p_data['price'],
                    'category': category,
                    'description': p_data['description'],
                    'stock': p_data['stock'],
                    'is_available': True
                }
            )
            status = "Created" if created else "Updated"
            print(f"📦 Product: {product.name} ({status}) at ₹{product.price} in {category.name}")
        else:
            print(f"❌ Error: Category {p_data['category_slug']} not found for product {p_data['name']}")

    print("✅ Database Sync Complete! 🗣️💎🚀🤴🤴🤴")

if __name__ == "__main__":
    seed_data()
