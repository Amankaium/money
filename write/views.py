from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import WaveForm
from .models import Wave

@login_required(login_url='login')
def write(request):

    form = WaveForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            wave = Wave()
            wave.user = request.user
            wave.money = form.cleaned_data['money']
            wave.description = form.cleaned_data['description']
            wave.save()

    return render(request, 'write/write.html', {
        'form': form,
    })
