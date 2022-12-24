from django.forms import ModelForm
from django import forms
from .models import Students

class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'},render_value=True)
        }