from django.shortcuts import render
from django.contrib import messages
from .models import Carousel
from .forms import CarouselModelForm


def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(status="published")
    # context['images'] = images
    return render(request, 'home/index.html', context)


# stuff not checked
def carousel_create(request):
    context = dict()
    context['form'] = CarouselModelForm()

    if request.method == 'POST':
        print(request.POST)
        print(request.FILES.get('cover_image'))
        carousel = Carousel.objects.create(
            title=request.POST.get('title')
        )
        messages.success(request, 'Birseyler eklendi ama ne oldu bilemiyorum')
    return render(request, 'manage/carousel_create.html', {})