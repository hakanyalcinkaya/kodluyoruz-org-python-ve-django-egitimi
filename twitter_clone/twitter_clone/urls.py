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

urlpatterns = [
    path('', welcome, ),
    path('index/', index, ),
    path('signup/', signup, ),
    path('logout/', logout_view, ),
    path('forget/', forget, ),
    path('forget/<slug:token>/', forget_password_check, ),
    path('admin/', admin.site.urls),

]
