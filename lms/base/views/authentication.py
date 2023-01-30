from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms import Form, CharField, EmailField, TextInput, PasswordInput


BootstrapInput = TextInput(attrs={"class": "form-control"})
BootstrapPasswordInput = PasswordInput(attrs={"class": "form-control"})


class RegistrationForm(Form):
    username = CharField(max_length=100, widget=BootstrapInput)
    email = EmailField(widget=BootstrapInput)
    password = CharField(max_length=100, widget=BootstrapPasswordInput)


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "login/login.html", {"login_error": False})

    username = request.POST.get("username", "")
    password = request.POST.get("password", "")

    user = authenticate(username=username, password=password)

    if not user:
        return render(request, "login/login.html", {"login_error": True})

    login(request, user)

    return redirect("/")


def registration_view(request: HttpRequest) -> HttpResponse:

    context = {
        "has_errors": False,
    }

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            return redirect("/login")
        else:
            context["has_errors"] = True

    context["form"] = RegistrationForm()
    return render(request, "login/registration.html", context)


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)

    return redirect("/")
