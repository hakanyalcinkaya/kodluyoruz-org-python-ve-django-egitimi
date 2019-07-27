from django.contrib import admin
from django.urls import path
from .views import (
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
    path('admin/', admin.site.urls),

]
