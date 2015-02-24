import uuid

from django.core.exceptions import PermissionDenied
from django.http import HttpResponseBadRequest
from django.utils.timezone import now
from django.views.generic import FormView

from .config import school_id
from .config import sso_key
from .config import base_url
from .crypto import Parchment
from .forms import ParchmentForm
from .utils import add_query_params


class ParchmentView(FormView):
    form_class = ParchmentForm
    template_name = 'parchment/login.html'

    connect_variables = {}
    required_variables = ('student_id', 'customers_firstname', 'customers_lastname')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            raise PermissionDenied
        return super(ParchmentView, self).dispatch(request, *args, **kwargs)

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
        p = Parchment(sso_key)
        return {'parch5': p.encrypt(self.connect_variables),
                'parchiv': p.iv,
                'debug': self.connect_variables['rand']}

    def get_context_data(self, **kwargs):
        context = super(ParchmentView, self).get_context_data(**kwargs)
        context['parchment_url'] = add_query_params(base_url, {'s_id': school_id})
        return context
