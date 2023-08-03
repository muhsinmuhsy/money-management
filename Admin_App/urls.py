from django.urls import path
from Admin_App.views import *

urlpatterns = [
    # ---------------------------------------------- Collector -------------------------------------------------------- #
    path('collector_list/', collector_list, name='collector_list'),
    path('collector_add/', collector_add, name='collector_add'),
    path('collector_edit/<int:collector_id>/', collector_edit, name='collector_edit'),
    path('collector_view/<int:collector_id>/', collector_view, name='collector_view'),
    path('collector_delete/<int:collector_id>/', collector_delete, name='collector_delete'),

    # ---------------------------------------------- Delivry Boy -------------------------------------------------------- #

    path('delivery_boy_list/', delivery_boy_list, name='delivery_boy_list'),
    path('delivery_boy_add/', delivery_boy_add, name='delivery_boy_add'),
    path('delivery_boy_edit/<int:delivery_boy_id>/', delivery_boy_edit, name='delivery_boy_edit'),
    path('delivery_boy_view/<int:delivery_boy_id>/', delivery_boy_view, name='delivery_boy_view'),
    path('delivery_boy_delete/<int:delivery_boy_id>/', delivery_boy_delete, name='delivery_boy_delete'),

    # ---------------------------------------------- Customer -------------------------------------------------------- #

    path('customer_list/', customer_list, name='customer_list'),
    path('customer_add/', customer_add, name='customer_add'),
    path('customer_edit/<int:customer_id>/', customer_edit, name='customer_edit'),
    path('customer_view/<int:customer_id>/', customer_view, name='customer_view'),
    path('customer_delete/<int:customer_id>/', customer_delete, name='customer_delete'),
    
    # ---------------------------------------------- Wholesaler -------------------------------------------------------- #

    path('wholesaler_list/', wholesaler_list, name='wholesaler_list'),
    path('wholesaler_add/', wholesaler_add, name='wholesaler_add'),
    path('wholesaler_edit/<int:wholesaler_id>/', wholesaler_edit, name='wholesaler_edit'),
    path('wholesaler_view/<int:wholesaler_id>/', wholesaler_view, name='wholesaler_view'),
    path('wholesaler_paid/<int:wholesaler_id>/', wholesaler_paid, name='wholesaler_paid'),

    path('wholesaler_delete/<int:wholesaler_id>/', wholesaler_delete, name='wholesaler_delete'),

    # ---------------------------------------------- Order -------------------------------------------------------- #

    path('order_list/', order_list, name='order_list'),
    path('order_add/', order_add, name='order_add'),
    path('order_edit/<int:order_id>/', order_edit, name='order_edit'),
    path('order_delete/<int:order_id>/', order_delete, name='order_delete'),
    path('order_view/<int:order_id>/', order_view, name='order_view'),
    # for automatic field add
    path('get_customer_details/', get_customer_details, name='get_customer_details'),

    # ---------------------------------------------- Report -------------------------------------------------------- #

    path('report/', report, name='report'),

    # ---------------------------------------------- Salary -------------------------------------------------------- #

    path('salary_delivery_boy_list/', salary_delivery_boy_list, name='salary_delivery_boy_list'),
    path('salary_delivery_boy_salary_list/<int:delivery_boy_id>/', salary_delivery_boy_salary_list, name='salary_delivery_boy_salary_list'),
    path('salary_delivery_boy_delete/<int:salary_id>/', salary_delivery_boy_delete, name='salary_delivery_boy_delete'),

    # ---------------------------------------------- Purchase -------------------------------------------------------- #
    path('purchase_add/<int:wholesaler_id>/', purchase_add, name='purchase_add'),
    
    
]   