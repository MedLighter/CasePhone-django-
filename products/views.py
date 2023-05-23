from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from products.models import Product, ProductCategory, basket

def index(request):
    context = {
        'title': 'CasePhone'
    }
    return render(request, 'products/index.html', context)


def products(request):
    if 'value' in request.GET:
        if request.GET['value'] == 0:
            product = Product.objects.all()
            # return HttpResponseRedirect("/products")
        else:
            product = Product.objects.filter(category=request.GET['value'])
    else:
        product = Product.objects.all()

    context = {
        'title': 'CP - Каталог товаров',
        'products': product,
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)


def view_basket(request):
    ids = []
    cart = basket.objects.filter(user_id = request.user.id)    
    for obj in cart:
        ids.append(obj.products_id)
    products = Product.objects.filter(id__in=ids)
    summa = sum(Product.objects.get(id=item.products_id).price * item.amount for item in cart)
    
    context = {
        'products': products,
        'summa': summa
    }
    return render(request, 'products/basket.html', context=context)






# def add_product_in_basket(request, basket_id):
#     # product = Product.objects.filter(id = basket_id)
#     cart = basket.objects.get(products_id = basket_id, user_id = request.user.id)
#     # print('\n', cart.values(), '\n', len(cart))
#     if cart:
#         cart.amount += 1
#         cart.save()
#     else:
#         add_product = basket(amount = 1, products_id = basket_id, user_id = request.user.id)
#         add_product.save()
    
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def add_product_in_basket(request, basket_id):
    try:
        cart = basket.objects.get(products_id=basket_id, user_id=request.user.id)
        cart.amount += 1
        cart.save()
    except ObjectDoesNotExist:
        add_product = basket(amount=1, products_id=basket_id, user_id=request.user.id)
        add_product.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# def remove_product_in_basket(request, basket_id):
#     cart = basket.objects.get(products_id=basket_id, user_id=request.user.id)
#     cart.delete()
#     cart.save()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# def add_product_in_busket(request, product_id):
#     product = Product.objects.filter(id = product_id)


# def product_details(request, product_id):
#     product = Product.objects.filter(id = product_id)

#     context = {
#         'product': product
#     }
#     return render(request, 'products/product_details.html', context)

