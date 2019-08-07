from django.urls import path
from .views import carousel_create


urlpatterns = [
    path('carousel_create/', carousel_create, name='carousel_create'), 
] 