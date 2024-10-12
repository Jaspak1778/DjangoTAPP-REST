REST API:n CORS Määritykset

#terminal:
pip install django-cors-headers

#settings.py:
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

#esim:
CORS_ALLOWED_ORIGINS = [
    "https://www.esimerkki.com",
    "https://toinen-esimerkki.com",
]

