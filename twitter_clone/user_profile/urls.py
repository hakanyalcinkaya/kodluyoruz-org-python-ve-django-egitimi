from django.urls import path
from .views import (
    login_form, 
    signup, 
    logout_view, 
    forget, 
    forget_password_check,
)


urlpatterns = [
    path('login/', login_form, ),
    path('signup/', signup, ),
    path('logout/', logout_view, name='logout'),
    path('forget/', forget, ),
    path('forget/<slug:password_token>/', forget_password_check, ),
]