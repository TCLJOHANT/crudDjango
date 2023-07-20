#AUTOR:TCL JOHAN +
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Artista

# Create crear
def crear(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        genero = request.POST.get('genero')
        descripcion = request.POST.get('descripcion')
        artista = Artista(nombre=nombre, genero=genero, descripcion=descripcion)
        artista.save()
        return redirect('index')
 
# read  leer  
def index (request):
    artistas = Artista.objects.all()
    return render(request, 'index.html',{'artistas':artistas}) 


# update actualizar
def editar(request, id):
    artista = Artista.objects.get(id=id)
    if request.method == 'POST':
        artista.nombre = request.POST.get('nombre')
        artista.genero = request.POST.get('genero')
        artista.descripcion = request.POST.get('descripcion')
        artista.save()
        return redirect('index')
    return render(request, 'form/edicion.html', {'artista': artista})

# Delete eliminar
def eliminar (request,id):
    artista = Artista.objects.get(id=id)
    artista.delete()
    return redirect('index')
