# feedback/forms.py
from django import forms

class FeedbackForm(forms.Form):
    # Textbox for Student Name
    student_name = forms.CharField(max_length=100, label='Student name')

    # Radio buttons for selecting Sex
    SEX_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    sex = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.RadioSelect, label='Sex')

    # Dropdown menu for selecting course
    COURSE_CHOICES = [
        ('ASP-XML', 'ASP-XML'),
        ('DotNET', 'DotNET'),
        ('JavaPro', 'JavaPro'),
        ('Unix', 'Unix'),
        ('C,C++', 'C,C++'),
    ]
    course = forms.ChoiceField(choices=COURSE_CHOICES, label='Select Course')

    # Radio buttons for selecting Technical Coverage
    TECHNICAL_COVERAGE_CHOICES = [
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Average', 'Average'),
        ('Poor', 'Poor'),
    ]
    technical_coverage = forms.ChoiceField(choices=TECHNICAL_COVERAGE_CHOICES, widget=forms.RadioSelect, label='Technical Coverage')

    # Textbox for Suggestions
    suggestions = forms.CharField(widget=forms.Textarea, label='Suggestions', required=False)
