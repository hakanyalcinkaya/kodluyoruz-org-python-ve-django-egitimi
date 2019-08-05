from django.contrib import admin
from django.urls import include, path
from .views import (
    feed,    
    welcome,
)
from tweet.views import tweet_post, show_user_post


urlpatterns = [
    path('', welcome, ),
    path('feed/', feed, name='feed'),
    path('tweet/tweet-post/', tweet_post),
    path('u/<slug:user_name>/', show_user_post,),
    path('user/', include('user_profile.urls')),
    path('admin/', admin.site.urls),
]

