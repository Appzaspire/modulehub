from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def reg_otp(request):
    return render(request,"reg_otp.html")

def forgot_pass(request):
    return render(request,'forgot_pass.html')

def payment_module(request):
    return render(request,'payment_module.html')
