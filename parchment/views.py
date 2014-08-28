from urllib import urlencode

from django.conf import settings
from django.views.generic import FormView

from .crypto import Parchment
from .forms import ParchmentForm


class ParchmentView(FormView):
    form_class = ParchmentForm
    template_name = 'parchment/login.html'
    connect_variables = {}

    def get(self, request, *args, **kwargs):
        for k, v in request.GET.items():
            self.connect_variables[k] = v
        return super(ParchmentView, self).get(request, *args, **kwargs)

    def get_initial(self):
        sso_key = getattr(settings, 'PARCHMENT_SSO_KEY')
        p = Parchment(sso_key)
        return {'parch5': p.encrypt(urlencode(self.connect_variables)),
                'parchiv': p.iv}
