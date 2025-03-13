# book_vote/forms.py
from django import forms

class VoteForm(forms.Form):
    CHOICES = [
        ('Good', 'Good'),
        ('Satisfactory', 'Satisfactory'),
        ('Bad', 'Bad'),
    ]
    vote = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=True)
