from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'Invalid credentials. Please try again.'
    else:
        error = None
    return render(request,'Authentication/sign-in.html', {'error' : error})

def logout_view(request):
    logout(request)
    return redirect('dashboard')