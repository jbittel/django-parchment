DEBUG = False
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'UTC'
USE_TZ = True

SECRET_KEY = '%y_&r=m-7hruwdgj*0w1y*b^l%-m_4593=)22k!g^_=npt&)t9'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'parchment',
)

PARCHMENT_SCHOOL_ID = '1234567890abcdef'
PARCHMENT_SSO_KEY = 'dpYeodnsgmaOav5fsqN7bhZM8W8hoaBM'
PARCHMENT_DEBUG_MODE = True
