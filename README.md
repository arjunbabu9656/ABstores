# ABstores - Premium Django E-commerce

A modern, high-performance, and responsive e-commerce platform built with Django. Featured with a "Code-as-the-Brain" database controller for seamless updates.

## 🚀 Key Features

- **Classic 2-Column Mobile Layout**: Inspired by giants like Amazon and Flipkart for a professional, dense catalog experience.
- **Glassmorphic Dark Theme**: Premium, modern aesthetics with sophisticated UI/UX.
- **Permanent Cloud Storage**: Integrated with **Cloudinary** for persistent media and **Neon.tech** for long-term data storage.
- **Code-Driven Sync**: Manage your entire catalog through `seed_db.py`. No manual database work required!
- **Zero-Sleep System**: Configured with Uptime Monitoring to stay awake 24/7 on Render.

## 🧠 Database Controller (seed_db.py)

Instead of using a complex database manager, you can manage your store directly in the Python code.

1.  Open `seed_db.py`.
2.  Edit the `products_data` or `categories_data` lists to change prices, names, or move items to new categories.
3.  **Push to GitHub.**
4.  Render will automatically sync your database using `update_or_create` logic based on product **slugs**.

## ⚙️ Environment Variables

To make the store fully permanent and functional, ensure the following are set in your Render dashboard:

| Variable | Description |
| :--- | :--- |
| `DATABASE_URL` | Your Neon.tech connection string. |
| `SECRET_KEY` | A unique string for security. |
| `CLOUDINARY_CLOUD_NAME` | Your Cloudinary account name. |
| `CLOUDINARY_API_KEY` | Your Cloudinary API key. |
| `CLOUDINARY_API_SECRET` | Your Cloudinary API secret key. |

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: Vanilla HTML5, CSS3, JavaScript
- **Database**: PostgreSQL (Production) / MySQL (Local)
- **Media**: Cloudinary
- **Deployment**: Render

---
🛡️ **Built with 💎 and 🚀 for Arjun B.**
