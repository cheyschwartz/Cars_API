# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v%@m!!px%7lesg^z^v%z_b#1!smzlo#jd-c&&0)m$t(%odl^n7'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Schwartz07!'
    }
}

