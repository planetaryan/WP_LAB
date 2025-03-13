# billing/forms.py
from django import forms

class BillingForm(forms.Form):
    BRANDS = [
        ('HP', 'HP'),
        ('Nokia', 'Nokia'),
        ('Samsung', 'Samsung'),
        ('Motorola', 'Motorola'),
        ('Apple', 'Apple'),
    ]
    
    item = forms.ChoiceField(choices=BRANDS, widget=forms.RadioSelect, label="Select Mobile Brand")
    categories = forms.MultipleChoiceField(
        choices=[('Mobile', 'Mobile'), ('Laptop', 'Laptop')],
        widget=forms.CheckboxSelectMultiple,
        label="Select Items",
    )
    quantity = forms.IntegerField(label="Quantity", min_value=1)
