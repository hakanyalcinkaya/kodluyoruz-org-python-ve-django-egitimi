from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.crypto import get_random_string
from user_profile.models import PasswordToken


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
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        error = False
        if password1 != password2:
            messages.warning(request, "Sifreniz yanlis")
            error = True
        if User.objects.filter(email=email).count():
            messages.warning(request, "E-mail adresiniz mevcut")
            error = True
        if User.objects.filter(username=username).count():
            messages.warning(request, "Kullanici Adi mevcut")
            error = True
        
        if error:
            return redirect('/signup/')

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


def forget(request):
    if request.method == "POST":
        email = request.POST.get('email')
        token = get_random_string(length=16).lower()
        # user = User.objects.get(email=email)
        user = get_object_or_404(User, email=email)
        pass_token = PasswordToken.objects.create(
            user=user,
            token=token,
        )
        messages.success(request, 'mail gonderildi')
        return redirect('/')
    return render(request, 'forget.html', dict() )


def forget_password_check(request, token):
    print(token)
    token_obj = get_object_or_404(
        PasswordToken, token=token
    )
    
    return render(
        request, 
        'forget_password_check.html',
        {'token': token_obj}
        )