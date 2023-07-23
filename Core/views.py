from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from U_Auth.models import User
from Admin_App.models import *
from django.db import IntegrityError
from django.contrib import messages

# Create your views here.

@login_required
def dashboard(request):
    order_count = Order.objects.count()
    customer_count = Customer.objects.count()
    collector_count = User.objects.filter(is_collector=True).count()
    delivery_boy_count = User.objects.filter(is_delivery_boy=True).count()

    collector_orders = Order.objects.filter(collector_name=request.user).order_by('-id')
    delivery_boy_orders = Order.objects.filter(delivery_boy_name=request.user).order_by('-id')
    context = {
        'order_count' : order_count,
        'customer_count' : customer_count,
        'collector_count' : collector_count,
        'delivery_boy_count' : delivery_boy_count,

        'collector_orders' : collector_orders,
        'delivery_boy_orders' : delivery_boy_orders,
        
    }
    return render(request,'Core/dashboard.html', context)

@login_required
def collector_order_view(request, order_id):
    order = Order.objects.get(id=order_id)
    context = {
        'order' : order,
    }
    return render(request, 'Core/collector_order_view.html', context)


@login_required
def delivery_boy_order_view(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.confirm_cancel_pending = request.POST.get('confirm_cancel_pending') 
        order.comment = request.POST.get('comment')
        try:
            order.save()
            messages.success(request, f"Done")
            return redirect('dashboard')
        except IntegrityError:
            messages.error(request, f"Faield")
    context = {
        'order' : order,
    }
    return render(request, 'Core/delivery_boy_order_view.html', context)


 

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