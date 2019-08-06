from django.shortcuts import render

def index(request):
    context = dict()
    return render(request, 'home/index.html', context)