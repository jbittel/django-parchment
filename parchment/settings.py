from django.conf import settings


parch_url = getattr(settings, 'PARCHMENT_URL',
                    'https://exchange.parchment.com/send/adds/index.php?main_page=sso')
debug_url = getattr(settings, 'PARCHMENT_DEBUG_URL',
                    'https://int-exchange.parchment.com/send/adds/index.php?main_page=sso')
