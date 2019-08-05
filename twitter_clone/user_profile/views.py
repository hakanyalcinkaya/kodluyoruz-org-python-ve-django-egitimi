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


def login_form(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Giris isleminiz basarili")
            else:
                error = f"{username} kullanici adi veya sifre dogrulanamadi"
                messages.warning(request, error)
        else:
            messages.warning(
                request, 
                "Lutfen kullanici adi ve sifre giriniz"
            )
    else:
        messages.info(request, 'naaptini anlamadim :(')
            
    return redirect('/')



def logout_view(request):
    logout(request)
    messages.info(request, 'Cikis Yaptiniz')
    return redirect('/')


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



# user
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
        # twitter.com/forget/hrhrhrdkzfhsdkzhfs/
        # localhost:8000/forget/<slug:token>/
        # localhost:8000/forget/1111/
        # localhost:8000/forget/<id:token>/
        messages.success(request, 'mail gonderildi')
        return redirect('/')
    return render(request, 'forget.html', dict() )


# user
def forget_password_check(request, password_token):
    # token_obj = get_object_or_404(
    #     PasswordToken, token=token
    # )

    token_obj = PasswordToken.objects.get(
        token=password_token
    )
    
    return render(
        request, 
        'forget_password_check.html',
        {'token': token_obj}
        )