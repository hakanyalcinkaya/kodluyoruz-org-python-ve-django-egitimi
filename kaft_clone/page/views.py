from django.shortcuts import render
from django.contrib import messages
from .models import Carousel

def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(status="published")
    # context['images'] = images
    return render(request, 'home/index.html', context)


# stuff not checked
def carousel_create(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES['cover_image'])
        messages.success(request, 'Birseyler eklendi ama ne oldu bilemiyorum')
    return render(request, 'manage/carousel_create.html', {})