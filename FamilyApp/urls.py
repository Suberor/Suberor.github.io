from django.urls import path
from FamilyApp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", iniciar_sesion, name="IniciarSesion"),
    path("logout/", LogoutView.as_view(template_name="FamilyApp/logout.html"), name="CerrarSesion"),
    path("registrar/", registro, name="Registrarse"),
    path("editar/", editar_usuario, name = "EditarUsuario"),
    path("agregar/", agregar_avatar, name = "CambiarAvatar"),
    path("inicio/", inicio, name="inicio"),
    path("soon/", proximamente, name="Soon"),
    path("opinar/<pk>", reseña_hechizos, name="reseña"),
    path("buscar/", buscar, name="buscar"),
    path("about/", about, name="about"),

    #paths de CRUD para hechizos usando clases
    
    path("hechizos/lista/", SeeSpells.as_view(), name="ListaHechizos"),
    path("hechizos/<int:pk>", DetailsSpells.as_view(), name="DetallesHechizos"),
    path("hechizos/crear/", CreateSpells.as_view(), name="CrearHechizos"),
    path("hechizos/editar/<int:pk>", UpdateSpells.as_view(), name="EditarHechizos"),
    path("hechizos/borrar/<int:pk>", DeleteSpells.as_view(), name="BorrarHechizos"),
    #path("hechizos/calificar/<int:pk>", RateSpells.as_view(), name="CalificarHechizos"),

    #paths de CRUD para armas usando clases

    path("armas/lista/", SeeWeapons.as_view(), name="ListaArmas"),
    path("armas/<int:pk>", DetailsWeapons.as_view(), name="DetallesArmas"),
    path("armas/crear/", CreateWeapons.as_view(), name="CrearArmas"),
    path("armas/editar/<int:pk>", UpdateWeapons.as_view(), name="EditarArmas"),
    path("armas/borrar/<int:pk>", DeleteWeapons.as_view(), name="BorrarArmas"),
    #path("armas/calificar/<int:pk>", RateWeapons.as_view(), name="CalificarArmas"),
]