from django import forms
class movieform(forms.Form):
    movie = forms.CharField(max_length=100)
    year = forms.IntegerField()