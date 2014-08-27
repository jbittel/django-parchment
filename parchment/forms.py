from django import forms


class ParchmentForm(forms.Form):
    parch5 = forms.CharField(widget=forms.HiddenInput)
    parchiv = forms.CharField(widget=forms.HiddenInput)
