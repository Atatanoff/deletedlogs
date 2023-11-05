from django import forms
from .models import TrackDel


class UserForm(forms.Form):
    server = forms.CharField(required=False)
    file_name = forms.CharField(required=False)
    dt_time = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}))
    to_dt_time = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}))
    user_name = forms.CharField(required=False)
