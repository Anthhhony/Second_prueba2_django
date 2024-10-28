from django.shortcuts import render, redirect
from finalApp2.models import DBproyecto
from . import forms
from finalApp2.forms import FormularioChetado

def vista(request):
    todo = DBproyecto.objects.all()
    data = {'registro':todo}
    return render(request, "templatesApp/index.html", data)

def registrar(request):
    form = forms.formulario()
    if request.method == "POST":
        form = forms.formulario(request.POST)
        if form.is_valid():
            db = DBproyecto(
                rut=form.cleaned_data['rut'],
                nombre=form.cleaned_data['nombre'],
                telefono=form.cleaned_data['telefono'],
                edad=form.cleaned_data['edad'],
                correo=form.cleaned_data['correo'],
            )
            db.save()
    data = {'form':form}
    return render(request,"templatesApp/registrar.html",data)

def eliminar(request, id):
    dato = DBproyecto.objects.get(id=id)
    dato.delete()
    return redirect("../")

def actualizar(request, id):
    project = DBproyecto.objects.get(id=id)
    form = FormularioChetado(instance=project)
    if request.method == "POST":
        form = FormularioChetado(request.POST, instance=project)
        if form.is_valid():
            form.save()
    data = {"form":form}
    return render(request,"templatesApp/registrar.html", data)
            
            

    

# Create your views here.
