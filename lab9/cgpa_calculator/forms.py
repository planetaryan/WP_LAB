# cgpa_calculator/forms.py
from django import forms

class CGPAForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name', required=True)
    total_marks = forms.IntegerField(label='Total Marks', required=True)
