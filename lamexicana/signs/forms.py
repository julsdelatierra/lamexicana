from django import forms
from models import Sign

class SignForm(forms.ModelForm):
    class Meta:
        model = Sign
        fields = ('name', 'email')
    
