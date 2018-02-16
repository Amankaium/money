from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .forms import UserForm

from write import views as write_views


@login_required(login_url='login')
def home(request):
    return redirect(write_views.write)

def sign_up(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            ))

            return redirect(home)

    return render(request, 'main/reg.html', {
        'form': form,
    })
