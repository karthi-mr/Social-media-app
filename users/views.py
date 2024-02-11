from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from users.forms import LoginForm, ProfileEditForm, RegistrationForm, UserEditForm
from users.models import Profile


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


def user_register(request):
    if request.method == 'POST':
        userForm = RegistrationForm(request.POST)
        if userForm.is_valid():
            newUser = userForm.save(commit=False)
            if not userForm.check_password():
                userForm.add_error("password", "Password doesn't match")
                return render(
                    request,
                    "users/register.html",
                    {"user_form": userForm, "error_message": userForm.errors},
                )
            newUser.set_password(userForm.cleaned_data['password'])
            newUser.save()
            Profile.objects.create(user=newUser)
            return render(
                request,
                "users/register.html",
                {"user_form": userForm, "register_success": True},
            )
        else:
            return render(
                request,
                "users/register.html",
                {"user_form": userForm, "error_message": userForm.errors},
            )
    userForm = RegistrationForm()
    return render(request, "users/register.html", {"user_form": userForm})


@login_required
def user_edit(request):
    if request.method == 'POST':
        userForm = UserEditForm(instance=request.user, data=request.POST)
        profileForm = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
    else:
        userForm = UserEditForm(instance=request.user)
        profileForm = ProfileEditForm(instance=request.user.profile)
    return render(
        request,
        "users/edit.html",
        {
            "user_form": userForm,
            "profile_form": profileForm,
        },
    )
