from django import forms
from django.contrib.auth.models import User

from users.models import Profile


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("profile_image",)


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

    def check_password(self):
        if self.cleaned_data["password"] != self.cleaned_data["password2"]:
            return None
            # raise forms.ValidationError("Password doesn't match")
        return self.cleaned_data["password2"]
