from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import Aprendizform
from .models import Aprendiz
from. import models

# Create your views here.

def principal(request):
    return render(request, 'principal.html')


def aprendices(request):
    aprendiz = models.Aprendiz.objects.all()
    return render(request, 'aprendices.html',{'aprendiz':aprendiz})


def agregar(request):
    if request.method == 'POST':
        print(request.POST)
        form = Aprendizform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('principal')
        else:
            print(form.errors)
    else:
        form = Aprendizform()
    return render(request, 'agregar.html', {'form': form})


def editar(request,id):
    aprendiz = Aprendiz.objects.get(id=id)
    form= Aprendizform(request.POST or  None, instance=aprendiz)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('aprendices')
    return render(request, 'editar.html', {'form': form})

def eliminar(request,id):
    eliminar=get_object_or_404(Aprendiz,pk=id)
    eliminar.delete()
    return redirect('aprendices')