from django.shortcuts import render
from django.db.models import Sum
from write.models import Wave
from .forms import ReportFilterForm

def report(request):

    waves = Wave.objects.filter(user=request.user)

    form = ReportFilterForm(request.GET)

    if form.is_valid():

        if form.cleaned_data["min_date"]:
            waves = waves.filter(date__gte=form.cleaned_data["min_date"])

        if form.cleaned_data["max_date"]:
            waves = waves.filter(date__lte=form.cleaned_data["max_date"])

        if form.cleaned_data["min_money"]:
            waves = waves.filter(money__gte=form.cleaned_data["min_money"])

        if form.cleaned_data["max_money"]:
            waves = waves.filter(money__lte=form.cleaned_data["max_money"])

    return render(request, 'report/report.html', {
        'waves': waves,
        'form': form,
        'sum': waves.aggregate(Sum('money'))['money__sum'],
    })
