from django import forms
from .models import User,Registration



class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','phone_number','password')
        widgets = {
            'password':forms.PasswordInput(),
        }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        exclude = ('user',)

