from django.conf import settings


if getattr(settings, 'PARCHMENT_DEBUG_MODE', False):
    url = getattr(settings, 'PARCHMENT_URL',
                  'https://exchange.parchment.com/send/adds/index.php?main_page=sso')
else:
    url = getattr(settings, 'PARCHMENT_DEBUG_URL',
                  'https://int-exchange.parchment.com/send/adds/index.php?main_page=sso')
