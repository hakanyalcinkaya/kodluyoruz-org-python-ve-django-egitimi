from django.contrib import admin
from django.urls import path
from .views import (
    index,    
    signup,
    logout_view,
    welcome,
    forget,
)

urlpatterns = [
    path('', welcome, ),
    path('index/', index, ),
    path('signup/', signup, ),
    path('logout/', logout_view, ),
    path('forget/', forget, ),
    path('admin/', admin.site.urls),

]
