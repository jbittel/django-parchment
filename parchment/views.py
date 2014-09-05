import uuid

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
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
    parch_url = 'https://exchange.parchment.com/send/adds/index.php?main_page=sso'
    required_variables = ('student_id', 'customers_firstname', 'customers_lastname')

    def get(self, request, *args, **kwargs):
        for var in self.required_variables:
            if var not in request.GET:
                return HttpResponseBadRequest("%s is required" % var)
        self.build_connect_string(request)
        return super(ParchmentView, self).get(request, *args, **kwargs)

    def build_connect_string(self, request):
        self.connect_variables = request.GET.dict()
        self.connect_variables['ts'] = now().isoformat()
        self.connect_variables['rand'] = uuid.uuid4()

    def get_initial(self):
        sso_key = getattr(settings, 'PARCHMENT_SSO_KEY', None)
        if sso_key is None:
            raise ImproperlyConfigured(
                'PARCHMENT_SSO_KEY must be configured with your provided '
                'SSO key')
        p = Parchment(sso_key)
        return {'parch5': p.encrypt(self.connect_variables),
                'parchiv': p.iv,
                'debug': self.connect_variables['rand']}

    def get_context_data(self, **kwargs):
        context = super(ParchmentView, self).get_context_data(**kwargs)
        school_id = getattr(settings, 'PARCHMENT_SCHOOL_ID', None)
        if school_id is None:
            raise ImproperlyConfigured(
                'PARCHMENT_SCHOOL_ID must be configured with your provided '
                '16 character organization identifier')
        url = getattr(settings, 'PARCHMENT_URL', self.parch_url)
        context['parchment_url'] = add_query_params(url, {'s_id': school_id})
        return context
