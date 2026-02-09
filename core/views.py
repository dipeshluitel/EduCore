from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request,'core/login.html')

def register_view(request):
    return render(request,'core/registration.html')

def dashboard(request):
    return render(request,'core/dashboard.html')