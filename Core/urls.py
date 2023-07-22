from django.urls import path
from Core.views import *

urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('profile/', profile, name='profile')
]