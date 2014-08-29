from urllib import urlencode
import uuid

from django.conf import settings
from django.http import HttpResponseBadRequest
from django.utils.timezone import now
from django.views.generic import FormView

from .crypto import Parchment
from .forms import ParchmentForm
from .utils import add_query_params


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

    def get_connect_string(self):
        self.connect_variables['ts'] = now().isoformat()
        self.connect_variables['rand'] = uuid.uuid4()
        return urlencode(self.connect_variables)

    def get_initial(self):
        sso_key = getattr(settings, 'PARCHMENT_SSO_KEY')
        p = Parchment(sso_key)
        return {'parch5': p.encrypt(self.get_connect_string()),
                'parchiv': p.iv}

    def get_context_data(self, **kwargs):
        context = super(ParchmentView, self).get_context_data(**kwargs)
        school_id = getattr(settings, 'PARCHMENT_SCHOOL_ID')
        url = 'https://int-exchange.parchment.com/send/adds/index.php?main_page=sso'
        context['parchment_url'] = add_query_params(url, {'s_id': school_id})
        return context
