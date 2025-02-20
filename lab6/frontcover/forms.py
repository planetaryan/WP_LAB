from django import forms

class MagazineForm(forms.Form):
    title = forms.CharField(max_length=100, label='Magazine Title')
    subtitle = forms.CharField(max_length=100, label='Subtitle')
    image = forms.ImageField(label='Upload Image')
    bg_color = forms.CharField(max_length=7, label='Background Color (Hex)', required=False)
    font_size = forms.IntegerField(label='Font Size', initial=30)
    font_color = forms.CharField(max_length=7, label='Font Color (Hex)', required=False)
