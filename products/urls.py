from django.urls import path

from products.views import products, view_basket, add_product_in_basket

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('basket/', view_basket, name='basket'),
    path('add_product_in_basket/<int:basket_id>', add_product_in_basket, name='add_product_in_basket'),
    # path('product_details/<int:product_id>', product_details, name='product_details'),
]
