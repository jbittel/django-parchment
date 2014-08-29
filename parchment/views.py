from urllib import urlencode

from django.conf import settings
from django.http import HttpResponseBadRequest
from django.views.generic import FormView

from .crypto import Parchment
from .forms import ParchmentForm


class ParchmentView(FormView):
    form_class = ParchmentForm
    template_name = 'parchment/login.html'
    connect_variables = {}
    required_variables = ('student_id', 'customers_firstname', 'customers_lastname')

    def get(self, request, *args, **kwargs):
        for var in self.required_variables:
            if var not in request.GET:
                return HttpResponseBadRequest("%s is required" % var)
        self.connect_variables = request.GET.dict()
        return super(ParchmentView, self).get(request, *args, **kwargs)

    def get_initial(self):
        sso_key = getattr(settings, 'PARCHMENT_SSO_KEY')
        p = Parchment(sso_key)
        return {'parch5': p.encrypt(urlencode(self.connect_variables)),
                'parchiv': p.iv}
