from django.contrib import admin

from products.models import ProductCategory, Product, basket

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(basket)
