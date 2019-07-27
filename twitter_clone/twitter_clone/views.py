from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def logout_view(request):
    logout(request)
    return redirect('/')


def welcome(request):
    template = "welcome.html"
    context = dict()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context['error'] = f"{username} kullanici adi veya sifre dogrulanamadi"

    if request.user.is_authenticated:
       template = "index.html"
    
    
    context['irfan'] = [
        'name1',
        'name2',
    ]
    return render(request, template, context)


def index(request):
    context = dict()
    return render(request, 'index.html', context)


def signup(request):
    context = dict()
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            context['error'] = "Sifreniz yanlis"
            return render(request, 'signup.html', context)
        else:
            User.objects.create_user(
                username,
                email,
                password1
            )
            user = authenticate(
                username=username, 
                password=password1
            )
            if user is not None:
                login(request, user)
                return redirect('/')

    return render(request, 'signup.html', context)