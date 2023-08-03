from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from U_Auth.models import User
from Admin_App.models import *
from django.db import IntegrityError
from django.contrib import messages
from datetime import date
from django.utils import timezone

# Create your views here.

@login_required
def dashboard(request):
    
    order_count = Order.objects.count()
    customer_count = Customer.objects.count()
    collector_count = User.objects.filter(is_collector=True).count()
    delivery_boy_count = User.objects.filter(is_delivery_boy=True).count()
    # total_money_collected_all_times = Order.objects.aggregate(total_money_collected=models.Sum('money_collected'))['total_money_collected']

    today = date.today()

    # Filter orders for today and sum up the money_collected field
    # total_money_collected_today = Order.objects.filter(date=today).aggregate(total_money_collected=models.Sum('money_collected'))['total_money_collected']
    order_count_today = Order.objects.exclude(customer_name=None).filter(date=today).count()
    

    collector_orders = Order.objects.filter(collector_name=request.user).order_by('-id')
    delivery_boy_orders = Order.objects.filter(delivery_boy_name=request.user).order_by('-id')

    users = User.objects.all().order_by('-last_login')
    user_logins = [(u.username, u.last_login.astimezone(timezone.get_current_timezone()) if u.last_login is not None else None) for u in users]
    
    context = {
        'order_count' : order_count,
        'customer_count' : customer_count,
        'collector_count' : collector_count,
        'delivery_boy_count' : delivery_boy_count,
        # 'total_money_collected_all_times': total_money_collected_all_times,

        # 'total_money_collected_today': total_money_collected_today,  
        'order_count_today': order_count_today,
        
        'collector_orders' : collector_orders,
        'delivery_boy_orders' : delivery_boy_orders,

        'user_logins': user_logins,
        
        
    }
    return render(request,'Core/dashboard.html', context)

@login_required
def collector_order_view(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.collector_amount = request.POST.get('collector_amount')
        order.money_collected = request.POST.get('money_collected')
        order.money_pending = request.POST.get('money_pending')
        try:
            order.save()
            messages.success(request, f"Done")
            return redirect('collector_order_view', order_id=order.id)
        except IntegrityError:
            messages.error(request, f"Faield")
    context = {
        'order' : order,
    }
    return render(request, 'Core/collector_order_view.html', context)


@login_required
def delivery_boy_order_view(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delivery_status = request.POST.get('delivery_status') 
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

def delivery_boy_salary_view(request):
    salary = DeliveryBoySalary.objects.filter(delivery_boy_name=request.user).order_by('-id')
    context = {
        'salary' : salary,
    }
    return render(request, 'Core/delivery_boy_salary_view.html', context)



@login_required
def collector_customers_list(request):
    # Get the current authenticated collector
    collector = request.user  # Assuming you are using Django's built-in authentication

    # Get the list of customers associated with the collector's orders
    customers_list = Order.objects.filter(collector_name=collector).values_list('customer_name', flat=True).distinct()

    # Now you have a list of customer IDs associated with the collector's orders
    # You can fetch the actual Customer objects using the IDs
    customers = Customer.objects.filter(id__in=customers_list)

    context = {
        'customers': customers
    }
    return render(request, 'Core/collector_customers_list.html', context)

@login_required
def collector_customer_orders(request, customer_id):
    # Get the current authenticated collector
    collector = request.user  # Assuming you are using Django's built-in authentication

    # Get the customer associated with the provided customer_id
    customer = Customer.objects.get(id=customer_id)

    # Get the list of orders for the specific customer handled by the collector
    customer_orders = Order.objects.filter(collector_name=collector, customer_name=customer)

    total_money_collected = sum(order.money_collected if order.money_collected is not None else 0 for order in customer_orders)
    total_money_pending = sum(order.money_pending if order.money_pending is not None else order.total for order in customer_orders)

    
    context = {
        'customer': customer,
        'orders': customer_orders,
        'total_money_collected': total_money_collected,
        'total_money_pending': total_money_pending,
    }

    return render(request, 'Core/collector_customer_orders.html', context)



@login_required
def profile(request):
    user = request.user
    if user.is_superuser:
        role = 'Admin'
    elif user.is_collector:
        role = 'collection Agent'
    elif user.is_delivery_boy:
        role = 'Delivery Agent'
    else:
        role = 'User Not Found'
    
    context = {
        'user' : user,
        'role' : role,
    }
    return render(request, 'Core/profile.html', context)


