from django import forms
from.models import local

class shelf(forms.ModelForm):
    class Meta:
        model = local 
        fields= ['title','Author','year']
    
    
