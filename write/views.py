from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import WaveForm, ProfileForm
from .models import Wave
from mainapp.models import Profile
from datetime import datetime

@login_required(login_url='login')
def write(request):

    form = WaveForm()

    if request.method == 'POST':
        form = WaveForm(request.POST)
        if form.is_valid():
            wave = Wave()
            wave.user = request.user
            wave.money = form.cleaned_data['money']
            wave.description = form.cleaned_data['description']
            wave.save()

            profile = request.user.profile
            profile.balance = profile.balance - wave.money
            profile.save()

    return render(request, 'write/write.html', {
        'form': form,
    })

@login_required(login_url='login')
def balance(request):

    if not Profile.objects.filter(user=request.user).exists():
        profile = Profile()
        profile.user = request.user
        profile.time = datetime.now()
        profile.save()

    form = ProfileForm(instance=Profile.objects.get(user=request.user))

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            profile.time = datetime.now()
            profile.balance = form.cleaned_data['balance']
            profile.save()


    return render(request, 'write/balance.html', {
        'form': form,
    })
