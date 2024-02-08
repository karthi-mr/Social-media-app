from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from users.forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userData = form.cleaned_data
            user = authenticate(
                request,
                username=userData.get("username"),
                password=userData.get("password"),
            )
            if user:
                login(request, user)
                return redirect("users:index")
            else:
                return render(
                    request,
                    "users/login.html",
                    {"login_form": form, "error_message": "Invalid Credential"},
                )
    form = LoginForm()
    return render(request, "users/login.html", {"login_form": form})


def user_logout(request):
    logout(request)
    return render(request, "users/logout.html")


@login_required(login_url="login/")
def index(request):
    return render(request, "users/index.html")
