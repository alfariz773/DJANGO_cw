from django import forms
from .models import Booklet
class bookForm(forms.ModelForm):
    class Meta:
        model = Booklet
        fields = ['book', 'author']