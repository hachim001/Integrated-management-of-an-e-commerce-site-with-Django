from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'EMAIL'}))
    passwd1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
    passwd2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'CONFIRM PASSWORD'}))
class loginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    passwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))