from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import get_messages

# Create your views here.
def login_view(request):

    # TODO : #This is wrong( need to create custom users)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Please enter both username and password.")
            return redirect('loginview')
        username = username.lower()

        user = authenticate(request,username=username,password=password) 
        if user:
            login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect('dashboard')
        else:
            messages.error(request, "Email or Password seems to be wrong")
            return redirect('loginview')
        
    return render(request,'core/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        email = request.POST.get('email').lower()
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        # location = request.POST.get('location')
        # logo = request.POST.get('logo')

        if pass1 != pass2:
            messages.error(request, "Password don't match")
            return redirect('registerview')
        
        if User.objects.filter(username = username).exists():
            messages.error(request, "Username already exists")
            return redirect('registerview') 
        
        user = User.objects.create_user(
            username = username,
            email = email,
            password = pass1,
            # location = location,
            # logo = logo,
        )
        user.save()
        messages.success(request, "User Created Successfully, Please Login")
        return redirect("registerview")


    return render(request,'core/registration.html')

def logout_view(request):
    logout(request)
    storage = get_messages(request)
    for _ in storage:
        pass
    messages.success(request, "Logged Out, Please Login")
    return redirect('loginview')

def features_view(request):
    return render(request,'core/features.html')

@login_required(login_url='loginview')
def reviews_view(request):
    return render(request,'core/reviews.html')

def dashboard(request):
    return render(request,'core/dashboard.html')

@login_required(login_url='loginview')
def notes_view(request):
    return render(request,'core/notes.html')

# TODO: ADD Lock_icon above nav-bar that requires login required and remove them when logged in