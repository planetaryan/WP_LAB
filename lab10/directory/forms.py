from django import forms
from .models import Category, Page

# Form for Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'number_of_visits', 'number_of_likes']

# Form for Page
class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['category', 'title', 'url', 'views']
