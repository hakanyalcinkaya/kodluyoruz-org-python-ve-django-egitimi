from django.urls import path
from .views import (
    carousel_create,
    carousel_list,
    carousel_update,
)


urlpatterns = [
    path('carousel/list/', carousel_list, name='carousel_list'), 
    path('carousel/create/', carousel_create, name='carousel_create'), 
    path('carousel/update/<int:pk>/', carousel_update, name='carousel_update'), 
] 
