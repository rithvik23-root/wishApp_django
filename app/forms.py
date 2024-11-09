from django import forms
from .models import MyUser, Gift

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['gift_name']
