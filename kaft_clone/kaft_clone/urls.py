from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from page.views import index
from product.views import category_show

urlpatterns = [
    path('', index, name='index'), 
    path('<slug:category_slug>', category_show, name='category_show'),
    path('manage/', include('page.urls'), ), 
    path('cart/', include('cart.urls'), ), 
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)