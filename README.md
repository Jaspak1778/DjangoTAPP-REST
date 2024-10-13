REST Memo.

Jos halutaan ottaa yhteys Frontendillä API rajapintaan, React yms tai Django projekti asetetaan pilvipalveluun niin CORS tulee olla käytössä.

CORS Asennus Djangoon: (venv)omaprojekti>

    bash:
    pip install django-headers

Lisää INSTALLED_APPS-listaan:

    settings.py:
    INSTALLED_APPS = [
    ...
    'corsheaders',
    ...]

Lisää MIDDLEWARE-listan alkuun:

    settings.py:
    MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...]

Määritä sallitut alkuperät:

    settings.py:
    CORS_ALLOWED_ORIGINS = [
        "https://www.esimerkki.com",
        "https://toinen-esimerkki.com",
    ]

