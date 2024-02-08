from django.contrib.auth.views import (
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import path, reverse_lazy

from users import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user-login'),
    path('logout/', views.user_logout, name='user-logout'),
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='users/password_change_form.html',
            success_url=reverse_lazy('users:password-change-done'),
        ),
        name='password_change',
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
        name='password-change-done',
    ),
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='users/password_reset_form.html',
            success_url=reverse_lazy('users:password-reset-done'),
            email_template_name='users/password_reset_email.html',
        ),
        name='password-reset',
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password-reset-done',
    ),
    path(
        'reset/<uidb64>/<token>',
        PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html',
            success_url=reverse_lazy('users:password-reset-complete'),
        ),
        name='password-reset-confirm',
    ),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html'
        ),
        name='password-reset-complete',
    ),
]
