from django.conf.urls import patterns
from django.conf.urls import url

from .views import ParchmentView


urlpatterns = patterns('',
    url(r'^parchment/?$',
        ParchmentView.as_view(),
        name='parchment_login'),
)
