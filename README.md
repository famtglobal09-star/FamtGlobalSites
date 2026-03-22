# FAMT Consulting Website

A professional Django-based website for owcus, a leading consulting firm specializing in accounting, tax, and business incorporation services.

## Features

- **Responsive Design**: Modern, mobile-friendly design using Bootstrap 5
- **Service Showcase**: Dedicated pages for showcasing consulting services
- **Blog System**: Content management system for publishing insights and articles
- **Contact Form**: Integrated contact form for client inquiries
- **WhatsApp Integration**: Direct chat buttons for instant customer communication
- **Admin Panel**: Django admin interface for content management

## Technology Stack

- **Backend**: Django 5.2
- **Frontend**: HTML5, CSS3, Bootstrap 5, Font Awesome
- **Database**: SQLite (development) / PostgreSQL (production)
- **Deployment**: Ready for deployment on any Django-compatible hosting

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd consulting_site
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

### Admin Panel
- Access the admin panel at `/admin/`
- Login with superuser credentials
- Manage Services, Blog posts, and Contact inquiries

### Content Management
- **Services**: Add/edit consulting services with titles and descriptions
- **Blog Posts**: Create and publish insightful articles
- **Contacts**: View and manage client inquiries

## Project Structure

```
consulting_site/
├── consulting_site/          # Main Django project
│   ├── settings.py          # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── website/                 # Main app
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── urls.py             # App URL configuration
│   ├── admin.py            # Admin interface
│   └── migrations/         # Database migrations
├── templates/               # HTML templates
│   ├── base.html           # Base template with navigation
│   ├── home.html           # Home page
│   ├── about.html          # About Us page
│   ├── services.html       # Services page
│   ├── blog.html           # Blog listing
│   ├── blog_detail.html    # Blog detail page
│   └── contact.html        # Contact page
├── static/                  # Static files
│   ├── css/
│   │   └── style.css       # Custom styles
│   └── images/             # Image assets
└── db.sqlite3              # SQLite database
```

## Email Configuration

By default the project uses Django's console email backend (prints emails to the terminal). To send real email notifications when a user submits the contact form, set the following environment variables:

- `EMAIL_BACKEND` (e.g. `django.core.mail.backends.smtp.EmailBackend`)
- `EMAIL_HOST` (e.g. `smtp.gmail.com`)
- `EMAIL_PORT` (e.g. `587`)
- `EMAIL_USE_TLS` (e.g. `True`)
- `EMAIL_HOST_USER` (your SMTP username)
- `EMAIL_HOST_PASSWORD` (your SMTP password)
- `DEFAULT_FROM_EMAIL` (sender address, e.g. `no-reply@famtyglobal.com`)
- `CONTACT_RECIPIENT_EMAIL` (where contact form submissions should be sent)

Example (Windows PowerShell):

```powershell
$env:EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
$env:EMAIL_HOST='smtp.gmail.com'
$env:EMAIL_PORT='587'
$env:EMAIL_USE_TLS='True'
$env:EMAIL_HOST_USER='your-email@example.com'
$env:EMAIL_HOST_PASSWORD='your-email-password'
$env:CONTACT_RECIPIENT_EMAIL='info@famtglobal.com'
```

## WhatsApp Configuration

The website includes WhatsApp integration for direct customer communication. Configure the WhatsApp number using the environment variable:

- `WHATSAPP_NUMBER` (your business WhatsApp number, e.g. `15551234567`)

Example:

```powershell
$env:WHATSAPP_NUMBER='15551234567'
```

The WhatsApp buttons will appear on the homepage hero section and as a floating button on all pages.

## Deployment

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS` with your domain
3. Set up a production database (PostgreSQL recommended)
4. Configure static files serving
5. Set up environment variables for sensitive data
6. Use a WSGI server like Gunicorn
7. Set up a reverse proxy with Nginx

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is proprietary software owned by Entely Global.

## Contact

For technical support or inquiries:
- Email: info@entelyglobal.com
- Website: https://entelyglobal.com
