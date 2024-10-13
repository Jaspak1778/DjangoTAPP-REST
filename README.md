Memo.

Huom:
Poista SECRET KEYn näkyvyys oikeassa tuotanto ympäristössä.

REST API
Jos halutaan ottaa yhteys Frontendillä API rajapintaan, React yms tai Django projekti asetetaan pilvipalveluun niin CORS tulee olla käytössä.


bash:'CORS Asennus Djangoon: (venv)omaprojekti>'

    pip install django-headers

settings.py:'Lisää INSTALLED_APPS-listaan'

    
    INSTALLED_APPS = [
    ...
    'corsheaders',
    ...]

settings.py:'Lisää MIDDLEWARE-listan alkuun'
    
    MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...]

settings.py:'Määritä sallitut alkuperät'
    
    CORS_ALLOWED_ORIGINS = [
        "https://www.esimerkki.com",
        "https://toinen-esimerkki.com",
    ]

