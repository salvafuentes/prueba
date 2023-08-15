from django.shortcuts import render, redirect
from .models import *
from .forms import AutoForm

# Create your views here.

def homepageView(request):
    return render(request, 'homepage.html')

def subirauto(request):
    if request.method == "POST":
        form = AutoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('homepage')
    else:
        form = AutoForm()
    return render(request, 'subirauto.html', {'form':form})

def verautos(request):
    lista_autos= Auto.objects.all()
    return render(request, 'verautos.html', {'lista_autos':lista_autos})