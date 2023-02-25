from django.shortcuts import render
from FamilyApp.models import *
from FamilyApp.forms import *
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# vista para iniciar sesión

def iniciar_sesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contraseña)

            if user:

                login(request, user)

                return render(request, "FamilyApp/inicio.html", {"mensaje": f"Bienvenido nuevamente, {usuario}!"})

        else:

                return render(request, "FamilyApp/inicio.html", {"mensaje": f"Datos incorrectos."})
        
    else:

        form = AuthenticationForm()

    return render(request, "FamilyApp/login.html", {"formulario":form})


# vista para registar un usuario

def registro(request):

    if request.method == "POST":

        form = UsuarioRegistro(request.POST or None)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()

            return render(request, "FamilyApp/inicio.html", {"mensaje":f"{username} se ha unido al grupo!"})
        
    else:

        form = UsuarioRegistro()

    return render(request, "FamilyApp/registro.html", {"formulario":form})


# vista para editar usuarios


@login_required
def editar_usuario(request):

    usuario = request.user

    if request.method == "POST":

        form = EditarFormulario(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "FamilyApp/inicio.html")
        
    else:

        form = EditarFormulario(initial={
                "email": usuario.email,
                "first_name": usuario.first_name, 
                "last_name": usuario.last_name, 
                })

    return render(request, "FamilyApp/EditarUsuario.html", {"formulario": form, "usuario": usuario})


# vista para agregar avatar al usuario que inició sesión


@login_required
def agregar_avatar(request):

    if request.method == "POST":

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():

            usuario_actual = User.objects.get(username=request.user)

            avatar = Avatar(usuario=usuario_actual, imagen=form.cleaned_data["imagen"])

            avatar.save()

            return render(request, "FamilyApp/inicio.html")
        
    else:

        form = AvatarFormulario()

    return render(request, "FamilyApp/EditarAvatar.html", {"formulario":form})


# vista para añadir reseña de hechizos 

@login_required
def reseña_hechizos(request, pk):

    if request.method == 'POST':


        form=ReseñasFormulario(request.POST or None)

        if form.is_valid():

            informacion = form.cleaned_data

            hechizo_reseña = SpellsReseñas(usuario=request.user,nombre=informacion["nombre"],
                                     puntaje=informacion["puntaje"], opinion=informacion["opinion"])

            hechizo_reseña.save()

            return render(request, "FamilyApp/inicio.html")
    else:

        form=ReseñasFormulario()

    return render(request, "FamilyApp/spell_rate.html", {"formulario":form})


# vista para buscar resultados de la reseña 

def buscar(request):

    if request.GET["enviar"]:

        nombre=request.GET["enviar"]

        resultados=SpellsReseñas.objects.filter(nombre__icontains=nombre)

        return render(request, "FamilyApp/resultados.html",{"resultados":resultados, "busqueda":nombre})

    else:

        respuesta="No se ingresó un nombre para buscar."

    return HttpResponse(respuesta)



# Vista de inicio del blog 


def inicio(request):

    return render(request, "FamilyApp/inicio.html") 


# vista para páginas en desarrollo

def proximamente(request):

    return render(request, "FamilyApp/Soon.html") 


# vista about 

def about(request):

    return render(request, "FamilyApp/about.html")




def monsters(request):

    formulario1 = MonstersFormulario(request.POST or None)

    if request.method == "POST": 

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            monster = Monsters(nombre = info["nombre"],
                               nivel_desafio = info["nivel_desafio"],
                               terreno = info["terreno"])

            monster.save()

            return render(request, "FamilyApp/inicio.html/")
        

    return render(request, "FamilyApp/monstruos.html/", {"form1": formulario1})


# CRUD de hechizos realizado con clases 

class SeeSpells(ListView):

    model = Spells

class DetailsSpells(LoginRequiredMixin, DetailView):

    model = Spells

class CreateSpells(LoginRequiredMixin, CreateView):

    model = Spells 
    success_url = "/FamilyApp/hechizos/lista"
    fields = ["nombre", "nivel", "escuela", "descripcion", "imagen"]

class UpdateSpells(LoginRequiredMixin, UpdateView):

    model = Spells
    success_url = "/FamilyApp/hechizos/lista"
    fields = ["nombre", "nivel", "escuela", "descripcion"]

class DeleteSpells(LoginRequiredMixin, DeleteView):
    
    model = Spells
    success_url = "/FamilyApp/hechizos/lista"


# CRUD de armas realizado con clases 

class SeeWeapons(ListView):

    model = Weapons

class DetailsWeapons(LoginRequiredMixin, DetailView):

    model = Weapons

class CreateWeapons(LoginRequiredMixin, CreateView):

    model = Weapons 
    success_url = "/FamilyApp/armas/lista"
    fields = ["nombre", "tipo", "versatil", "legendaria", "descripcion", "imagen"]

class UpdateWeapons(LoginRequiredMixin, UpdateView):

    model = Weapons
    success_url = "/FamilyApp/armas/lista"
    fields = ["nombre", "tipo", "versatil"]

class DeleteWeapons(LoginRequiredMixin, DeleteView):
    
    model = Weapons
    success_url = "/FamilyApp/armas/lista"





