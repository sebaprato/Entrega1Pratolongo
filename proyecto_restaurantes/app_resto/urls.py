from django.urls import URLPattern, path
from . import views

urlpatterns = [

    path("",views.inicio),
    path("lista_restaurantes", views.lista_restaurantes),
    path("lista_platos", views.lista_platos),
    path("lista_reseñas", views.lista_reseñas),
    #path("alta_restaurantes", views.alta_restaurantes),
    #path("alta_platos", views.alta_platos),
    #path("alta_reseñas", views.alta_reseñas),
    path("alta_restaurantes", views.formulario_resto),
    path("alta_platos", views.formulario_plato),
    path("alta_reseñas", views.formulario_reseña),
    path("buscar_resto", views.buscador_resto),
    path("buscar" , views.buscar)

]