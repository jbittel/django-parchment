from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


if getattr(settings, 'PARCHMENT_DEBUG_MODE', False):
    url = getattr(settings, 'PARCHMENT_URL',
                  'https://exchange.parchment.com/send/adds/index.php?main_page=sso')
else:
    url = getattr(settings, 'PARCHMENT_DEBUG_URL',
                  'https://int-exchange.parchment.com/send/adds/index.php?main_page=sso')

sso_key = getattr(settings, 'PARCHMENT_SSO_KEY', None)
if sso_key is None:
    raise ImproperlyConfigured(
        'PARCHMENT_SSO_KEY must be configured with your provided '
        'SSO key')

school_id = getattr(settings, 'PARCHMENT_SCHOOL_ID', None)
if school_id is None:
    raise ImproperlyConfigured(
        'PARCHMENT_SCHOOL_ID must be configured with your provided '
        '16 character organization identifier')
