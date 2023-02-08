from django.shortcuts import render

from products.models import Product, ProductCategory

def index(request):
    context = {
        'title': 'CasePhone'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'CP - Каталог товаров',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
