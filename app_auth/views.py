from django.forms import fields
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout #Authentification de l'utilisateur et connexion
from django.contrib import messages #gestion de messag erreur ou reussite
from django.contrib.auth.models import User # Utilisateur
from .forms import *
# Create your views here.


def login_blog(request):
    """Fonction de connexion avec autehtification"""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = authenticate(username=username, password=pwd)

            #Verifier si les coordonnee sont correctes
            if user is not None:
                login(request, user)
                return redirect('dashbord')
            else:
                messages.error(request, "Authentification echoue")
                context = {"form": form}
                return render(request, 'login.html', context)

        else:
            context = {"form": form}
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
            return render(request, 'login.html', context)
    else:
        form = LoginForm()
        context = {"form": form}
        return render(request, "login.html", context)


def register(request):
    """Fonction d'enregistrement d'utilisateur"""
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = User.objects.create_user(username=username, password=pwd)

            #Verifier si la creation de compte a reussi
            if user is not None:
                return redirect("login-blog")
            else:
                messages.error(request, 'Creation de compte a echoue')
                context = {"form": form}
                return render(request, "register.html", context)

        else:
            context = {"form": form}
            return render(request, 'register.html', context)
        context = {"form": form}
        return render(request, 'register.html', context)

    form = RegisterForm()
    context = {"form": form}
    return render(request, 'register.html', context)



def register_blog(request):
    """dddddddd"""
    logout(request)
    return redirect("login-blog")



"""
def login_blog(request):
    if request.method == "POST":
        username = request.POST['username']
        pwd = request.POST["pwd"]
        user = authenticate(username=username, password=pwd)

        if user is not None:
            return redirect("home")
        else:
            messages.error(request, "Erreur d'authentification")
            return redirect("login-blog")
        print('Le nom est: ', username)
    return render(request, "login.html")

"""