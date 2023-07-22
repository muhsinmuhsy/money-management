from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from U_Auth.models import User

# Create your views here.

@login_required
def dashboard(request):
    return render(request,'Core/dashboard.html')

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