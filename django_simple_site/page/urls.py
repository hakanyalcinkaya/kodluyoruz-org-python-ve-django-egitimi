from django.urls import path
from .views import page


urlpatterns = [
    path('<slug:slug>/', page, ),
]
