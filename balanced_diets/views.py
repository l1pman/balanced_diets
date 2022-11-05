from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import New_kcal
from .forms import KcalForm


def index(request):
    kcal = New_kcal.objects.all()
    for i in kcal:
        if request.user.username == i.name:
            return render(request, 'balanced_diets/index.html', {"name": i.name})
    else:
        return render(request, 'balanced_diets/index.html')


def new_kcal(request):
    if request.method != 'POST':
        form = KcalForm()
    else:
        form = KcalForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('balanced_diets:my_diet')

    context = {'form': form}
    return render(request, 'balanced_diets/new_kcal.html', context)


def edit_kcal(request):
    kcal_id = request.user.username
    kcal = New_kcal.objects.get(name=kcal_id)
    if request.method != 'POST':
        form = KcalForm(instance=kcal)
    else:
        form = KcalForm(instance=kcal, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('balanced_diets:my_diet')
    context = {'kcal': kcal, 'form': form}
    return render(request, 'balanced_diets/edit_kcal.html', context)


@login_required
def my_diet(request):
    kcal = New_kcal.objects.all()
    for i in kcal:
        if request.user.username == i.name:
            kbzu = New_kcal.get_kcal(i)
            context = {
                "kal": kbzu[0],
                "belki": kbzu[1],
                "zhiri": kbzu[2],
                "ugl": kbzu[3],
            }
            return render(request, 'balanced_diets/my_diet.html', context)


    else:
        return render(request, 'balanced_diets/my_diet.html')
