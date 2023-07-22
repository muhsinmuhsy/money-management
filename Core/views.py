from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from U_Auth.models import User
from Admin_App.models import Order

# Create your views here.

@login_required
def dashboard(request):
    collector_orders = Order.objects.filter(collector_name=request.user).order_by('-id')
    delivery_boy_orders = Order.objects.filter(delivery_boy_name=request.user).order_by('-id')
    context = {
        'collector_orders' : collector_orders,
        'delivery_boy_orders' : delivery_boy_orders,
    }
    return render(request,'Core/dashboard.html', context)

 

@login_required
def profile(request):
    user = request.user
    if user.is_superuser:
        role = 'Superuser'
    elif user.is_collector:
        role = 'collector'
    elif user.is_delivery_boy:
        role = 'Delivery Boy'
    else:
        role = 'User Not Found'
    
    context = {
        'user' : user,
        'role' : role,
    }
    return render(request, 'Core/profile.html', context)