from django import forms
from .models import Works, Lives

# Form for inserting data into the WORKS table
class WorksForm(forms.ModelForm):
    class Meta:
        model = Works
        fields = ['person_name', 'company_name', 'salary']

# Form for inserting data into the LIVES table
class LivesForm(forms.ModelForm):
    class Meta:
        model = Lives
        fields = ['person_name', 'street', 'city']
