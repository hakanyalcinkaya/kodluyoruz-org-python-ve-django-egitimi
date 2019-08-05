from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.crypto import get_random_string
from tweet.models import TweetPost


def welcome(request):
    template = "welcome.html"
    context = dict()

    if request.user.is_authenticated:
       return redirect(feed)
    
    
    return render(request, template, context)


def feed(request):
    context = dict()
    tweets = TweetPost.objects.filter(
        is_deleted = False,
    ).order_by('-pk')
    context['tweets'] = tweets
    return render(request, 'index.html', context)
