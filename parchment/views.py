from django.conf import settings
from django.views.generic import FormView

from .crypto import Parchment
from .forms import ParchmentForm


class ParchmentView(FormView):
    form_class = ParchmentForm
    template_name = 'parchment/login.html'

    def get_initial(self):
        sso_key = getattr(settings, 'PARCHMENT_SSO_KEY')
        p = Parchment(sso_key)
        return {'parch5': p.encrypt('test string'),
                'parchiv': p.iv}
