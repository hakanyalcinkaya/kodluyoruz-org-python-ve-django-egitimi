from django.shortcuts import render
from django.contrib import messages
from .models import Carousel
from .forms import CarouselModelForm

# User:
def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(
        status="published",
    ).exclude(cover_image='')
    # context['images'] = images
    return render(request, 'home/index.html', context)


# Admin:
def carousel_list(request):
    context = dict()
    context['carousel'] = Carousel.objects.all().order_by('-pk')
    return render(request, 'manage/carousel_list.html', context)


def carousel_update(request, pk):
    context = dict()
    # kaft_clone.com/manage/carousel/1/edit
    item = Carousel.objects.get(pk=pk)
    context['form'] = CarouselModelForm(instance=item)
    return render(request, 'manage/carousel_form.html', context)


# stuff not checked
def carousel_create(request):
    context = dict()
    context['form'] = CarouselModelForm()
    
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES.get('cover_image'))
        # create code is deleted
        form = CarouselModelForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
        messages.success(request, 'Birseyler eklendi ama ne oldu bilemiyorum')
    return render(request, 'manage/carousel_form.html', context)