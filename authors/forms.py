from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password= forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder' :'Digite a senha'})
    )

class RegisterForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        

