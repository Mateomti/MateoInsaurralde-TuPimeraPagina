from django.shortcuts import render,redirect
from inicio.forms import RegistroProducto
from inicio.models import Producto


def inicio(request):
    return render(request, 'inicio.html')

def registro(request):
    formulario = RegistroProducto()
    if request.method == 'POST':
        formulario = RegistroProducto(request.POST)
        if formulario.is_valid():
            codigo = formulario.cleaned_data.get('codigo')
            nombre = formulario.cleaned_data.get('nombre')
            cantidad = formulario.cleaned_data.get('cantidad')
            formulario = Producto(codigo=codigo, nombre=nombre, cantidad=cantidad)
            formulario.save()
            return redirect('inicio')

    return render(request, 'registro.html', {'formulario': formulario})

def listado(request):
    lista = Producto.objects.all()
    return render(request, 'listado.html', {'lista':lista})