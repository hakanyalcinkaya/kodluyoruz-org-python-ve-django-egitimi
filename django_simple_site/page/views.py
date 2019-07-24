from django.shortcuts import render

def index_page(request):
    names = [
        '<strong>Kodluyoruz</strong>',
        '<strong>Apple</strong>',
        'Microsoft',
        'HP',
        'Dell',
        'Vakademi',
    ]
    context = {
        'names': names
    }
    return render(request, 'page/index.html', context)


def page(request, slug):
    context = {
        'title': f"{slug.upper()} PAGE"
    }
    return render(request, 'page/default_page.html', context)