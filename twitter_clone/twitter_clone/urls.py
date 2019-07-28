from django.contrib import admin
from django.urls import path
from .views import (
    forget,
    forget_password_check,
    index,    
    signup,
    logout_view,
    welcome,
)
from tweet.views import tweet_post, show_user_post


urlpatterns = [
    path('', welcome, ),
    path('index/', index, ),
    path('signup/', signup, ),
    path('logout/', logout_view, ),
    path('forget/', forget, ),
    path('forget/<slug:password_token>/', forget_password_check, ),
    path('tweet/tweet-post/', tweet_post),
    path('u/<slug:user_name>/', show_user_post,),
    path('admin/', admin.site.urls),

]
