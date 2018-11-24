from django import forms
import datetime

class SuggestForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    organization = forms.CharField(required=False)
    area = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    date = forms.DateField(required=False)
    suggestion = forms.CharField(widget=forms.Textarea)
