Kun Django REST API laitetaan pilveen (esim. Azure), tarvitaan CORS-määritykset:

CORS Määritykset

    Asennus:

    bash:
    pip install django-headers

settings.py:

    Lisää INSTALLED_APPS-listaan:

    python
    INSTALLED_APPS = [
    ...
    'corsheaders',
    ...]

Lisää MIDDLEWARE-listan alkuun:

    MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...]



Määritä sallitut alkuperät:

    CORS_ALLOWED_ORIGINS = [
        "https://www.esimerkki.com",
        "https://toinen-esimerkki.com",
    ]

