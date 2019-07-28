from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import TweetPost


@login_required
def tweet_post(request):
    if request.method == "POST":
        post = request.POST.get('tweet')
        created_tweet = TweetPost.objects.create(
            user=request.user,
            post=post,
        )
        if created_tweet:
            messages.success(request, 'Tweet Added')
        return redirect('/')


def show_user_post(request, user_name):
    user = User.objects.get(username=user_name)
    tweets = TweetPost.objects.filter(user=user).order_by('-pk')
    return render(
        request, 
        'user_posts.html', 
        {'tweets': tweets},
    )