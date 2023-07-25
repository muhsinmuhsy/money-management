from django.urls import path
from Core.views import *

urlpatterns = [
    path('',dashboard,name='dashboard'),

    path('collector_order_view/<int:order_id>/', collector_order_view, name='collector_order_view'),
    path('delivery_boy_order_view/<int:order_id>/', delivery_boy_order_view, name='delivery_boy_order_view'),

    path('delivery_boy_salary_view/', delivery_boy_salary_view, name='delivery_boy_salary_view'),

    path('profile/', profile, name='profile')

]