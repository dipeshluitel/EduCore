from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        user = authenticate(User,email=email,password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('loginview')
        
    return render(request,'core/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        email = request.POST.get('email').lower()
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        location = request.POST.get('location')
        logo = request.POST.get('logo')

        if pass1 != pass2:
            return redirect('registerview')
        
        if User.objects.filter(username = username).exists():
            return redirect('registerview') 
        
        user = User.objects.create(
            username = username,
            email = email,
            password = pass1,
            location = location,
            logo = logo,
        )
        user.save()
        return redirect(register_view)


    return render(request,'core/registration.html')

def dashboard(request):
    return render(request,'core/dashboard.html')