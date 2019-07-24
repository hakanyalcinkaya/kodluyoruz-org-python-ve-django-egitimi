from django.contrib import admin
from django.urls import path, include
from .views import (
    index,
    about_page,
) # ilk ornekte kullanildi

from page.views import index_page

urlpatterns = [
    # path('', index), # name kullanilmadi
    # path('about/', about_page),  # name kullanilmadi
    path('', index_page, name="index"),
    path('page/', include('page.urls')),
    path('admin/', admin.site.urls),
]
