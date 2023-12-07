from django.shortcuts import render
from restaurantes.models import Entrada,Comentario

# Create your views here.
def home(request):
    Prendas = Entrada.objects.all()
    if request.method == "POST":
        nombre = request.POST["nombre"]
        mensaje = request.POST["mensaje"]
        obj = Comentario(nombre=nombre,Comentario=mensaje)
        obj.save()
        mensaje = "Gracias por tu comentario"
        return render(request,"home.html",{"Restaurantes":Prendas,"mensaje":mensaje})
    return render(request,"home.html",{"Restaurantes":Prendas})
    

def conoce(request):
    Restaurantes = Entrada.objects.all()
    
    return render(request,"Conocenos.html")

def galeria(request):
    Restaurantes = Entrada.objects.all()
    
    return render(request,"Galeria.html")