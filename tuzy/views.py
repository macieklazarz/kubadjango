from django.http import HttpResponse
from django.shortcuts import render
from .models import Tuz

def tuzy_lista(request):
    tuzy = Tuz.objects.all().order_by('date')
    return render(request, 'tuzy/tuzy_lista.html', {'tuzy': tuzy})

# def tuz(request, slug):
#     return HttpResponse(slug)

def tuz(request, slug):
    #return HttpResponse(slug)
    tuz = Tuz.objects.get(slug=slug)
    return render(request,'tuzy/tuz.html',{'tuz': tuz})

