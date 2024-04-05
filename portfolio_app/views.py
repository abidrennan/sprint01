from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'portfolio_app/index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        myUser = User.objects.create_user(username, email, password1)
        myUser.first_name = firstname
        myUser.last_name = lastname

        myUser.save()

        messages.success(request, "Your account has been successfully created!")

        return redirect('login')


    return render(request, "portfolio_app/signup.html")

def login(request):
    return render(request, "portfolio_app/login.html")

def logout(request):
    pass