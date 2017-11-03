from django import forms

class LoginForm(forms.Form):
    """docstring for LoginForm."""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
