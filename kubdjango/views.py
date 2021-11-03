from django.http import HttpResponse
from django.shortcuts import render
from realizacje.models import Realizacje
from tuzy.models import Marka

def homepage(request):
    context = {}
    foto = Realizacje.objects.all()
    marki = Marka.objects.all()
    return render(request, 'index.html', {'foto':foto, 'marki':marki})
