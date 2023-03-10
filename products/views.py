from django.shortcuts import render

from products.models import Product, ProductCategory

def index(request):
    context = {
        'title': 'CasePhone'
    }
    return render(request, 'products/index.html', context)


def products(request):
    product = Product.objects.filter(category=request.GET['value'])
    context = {
        'title': 'CP - Каталог товаров',
        'products': product,
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
