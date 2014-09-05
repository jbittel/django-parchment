from django import forms
from django.conf import settings


class ParchmentForm(forms.Form):
    parch5 = forms.CharField(widget=forms.HiddenInput)
    parchiv = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super(ParchmentForm, self).__init__(*args, **kwargs)
        if getattr(settings, 'PARCHMENT_DEBUG_MODE', False):
            self.fields['debug'] = forms.CharField(widget=forms.HiddenInput)
