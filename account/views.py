from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from account.forms import RegisterForm, loginForm
from django.contrib.auth.models import User


# Create your views here.

def register_view(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('passwd1')
            password2 = form.cleaned_data.get('passwd2')
            
            if password1 != password2:
                messages.error(request, 'Passwords do not match.')
            
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
            
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already registered.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                login(request, user)
                messages.success(request, 'Registration successful.')
                return redirect('index')  
                
        else:
            messages.error(request, 'Registration failed. Please check the form data.')
    
    return render(request, 'account/register.html', {'form': form})




def logout_view(request):
    logout(request)
    return redirect('index')