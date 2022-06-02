from django.http import HttpResponse
from django.shortcuts import render
from app_resto.models import Restaurante
from app_resto.models import Platos
from app_resto.models import Reseñas
from django.template import loader



def inicio(request):

    return render( request , "plantillas.html" )


def lista_restaurantes(request):
    restaurantes = Restaurante.objects.all()
    dicc_resto = {"dicc_resto": restaurantes}

    return render(request , "lista_restaurantes.html", dicc_resto)

def alta_restaurantes(request):
    restaurante= Restaurante (nombre = "Pin Pun", categoria = "Pizzas" , ubicacion ="Lomas de Zamora" , capacidad = "250")
    restaurante.save()
    restaurante= Restaurante (nombre = "Figaro", categoria = "Empanadas" , ubicacion ="Lomas de Zamora" , capacidad = "100")
    restaurante.save()
    restaurante= Restaurante (nombre = "Sushi Club", categoria = "Sushi" , ubicacion ="Lomas de Zamora" , capacidad = "150")
    restaurante.save()
    restaurante= Restaurante (nombre = "Los Nonos", categoria = "Parrilla" , ubicacion ="Lomas de Zamora" , capacidad = "300")
    restaurante.save()

    return HttpResponse("Todo ok")


def lista_platos(request):
    platos = Platos.objects.all()
    dicc_plato = {"dicc_plato": platos}

    return render(request , "lista_platos.html", dicc_plato)


def alta_platos(request):
    plato= Platos (plato = "Milanesa napolitana", categoria = "Milanesas" , tipo ="Minuta" , precio = "1500")
    plato.save()
    plato= Platos (plato = "Lomo a la pimienta", categoria = "Parrilla" , tipo ="Gourmet" , precio = "2000")
    plato.save()
    plato= Platos (plato = "Pescado al roquefort", categoria = "Pescados" , tipo ="Menu Ejecutivo" , precio = "1700")
    plato.save()
    plato= Platos (plato = "Fideos con bolognesa", categoria = "Pastas" , tipo ="Menu Ejecutivo" , precio = "1100")
    plato.save()
   
    return HttpResponse("Todo ok")


def lista_reseñas(request):
    reseñas = Reseñas.objects.all()
    dicc_reseña = {"dicc_reseña": reseñas}

    return render(request , "lista_reseñas.html", dicc_reseña)

def alta_reseñas(request):
    reseña= Reseñas (plato = "Milanesa napolitana", sabor = "4" , presentacion ="3" , calidad_precio = "3")
    reseña.save()
    reseña= Reseñas (plato = "Lomo a la pimienta", sabor = "5" , presentacion ="2" , calidad_precio = "3")
    reseña.save()
    reseña= Reseñas (plato = "Pescado al roquefort", sabor = "3" , presentacion ="2" , calidad_precio = "1")
    reseña.save()
    reseña= Reseñas (plato = "Fideos a la bolognesa", sabor = "5" , presentacion ="5" , calidad_precio = "5")
    reseña.save()
   
   
    return HttpResponse("Todo ok")


def formulario_resto(request):

    if request.method == "POST":

        restaurante = Restaurante (nombre= request .POST['nombre'], categoria= request .POST['categoria'], ubicacion= request .POST['ubicacion'], capacidad= request .POST['capacidad'])
        restaurante.save()
        return render(request,"formulario_resto.html")

    return render(request,"formulario_resto.html")




def formulario_plato(request):

    if request.method == "POST":
         
        plato = Platos (plato= request .POST['plato'], categoria= request .POST['categoria'], tipo= request .POST['tipo'], precio= request .POST['precio'])
        plato.save()
        return render(request,"formulario_plato.html")
    
    return render(request,"formulario_plato.html")




def formulario_reseña(request):

    if request.method == "POST":
         
        reseña = Reseñas (plato= request .POST['plato'], sabor= request .POST['sabor'], presentacion= request .POST['presentacion'], calidad_precio= request .POST['calidad_precio'])
        reseña.save()
        return render(request,"formulario_reseña.html")

    return render (request, "formulario_reseña.html")


def buscador_resto(request):

    return render ( request, "buscador_resto.html")

def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        nombre = Restaurante.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"nombre": nombre})
    else:
        return HttpResponse("Campo vacio")