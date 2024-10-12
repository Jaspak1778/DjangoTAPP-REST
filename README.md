Kun Django REST API laitetaan pilveen (esim. Azure), tarvitaan CORS-määritykset:
REST API
CORS Määritykset

    Asennus:

    bash

pip install django-cors-headers

settings.py:

    Lisää INSTALLED_APPS-listaan:

    python

INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]

Lisää MIDDLEWARE-listan alkuun:

python

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

Määritä sallitut alkuperät:

python

    CORS_ALLOWED_ORIGINS = [
        "https://www.esimerkki.com",
        "https://toinen-esimerkki.com",
    ]
Tarkista myös!:
Turvallisuus,  Lisäasetukset.
