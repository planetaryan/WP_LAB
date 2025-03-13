# user_registration/forms.py
from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, required=False, label='Password')
    email = forms.EmailField(required=False, label='Email')
    contact_number = forms.CharField(max_length=15, required=False, label='Contact Number')
