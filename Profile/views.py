
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

from datetime import datetime


@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        organization_name = request.POST.get('organization_name')
        location = request.POST.get('location')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        

        if profile is None:
            user = User.objects.get(username=request.user.username)
            profile = Profile(user=user)

        profile.user.username = username
        profile.first_name = first_name
        profile.last_name = last_name
        profile.organization_name = organization_name
        profile.location = location
        profile.user.email = email
        profile.phone_number = phone_number
        

        profile.save()

        # Mettre à jour les champs username et email de l'objet User
        profile.user.username = username
        profile.user.email = email
        profile.user.save()

        return redirect('profile')
    else:
        return render(request, 'profile.html', {'profile': profile})