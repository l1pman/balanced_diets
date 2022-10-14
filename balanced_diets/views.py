from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from .models import User
from .forms import KcalForm

def index(request):
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

@login_required
def my_diet(request):
    return render(request, 'balanced_diets/my_diet.html')