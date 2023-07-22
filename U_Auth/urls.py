from django.urls import path
from U_Auth.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sign-in/', sign_in, name='sign-in'),
    path('logout/', logout_view, name='logout'),

    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='Authentication/password_change.html'), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='Authentication/password_change_done.html'), name='password_change_done'),
]