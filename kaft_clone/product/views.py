from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from page.views import STATUS

def category_show(request, category_slug):
    context = dict()
    context['category'] = get_object_or_404(Category, slug=category_slug)
    
    # # Nav:
    # context['categories'] = Category.objects.filter(
    #     status=STATUS
    # ).order_by('title')
    context['items'] = Product.objects.filter(
        category=context['category'],
        status=STATUS,
        stock__gte=1,
    )

    return render(request, 'product/category_show.html', context)