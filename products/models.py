from django.db import models
from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_img')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT )

    def __str__(self):
        return f'Товар: {self.name} | Описание: {self.description}'


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class basket(models.Model):
    amount = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    products = models.ForeignKey(to=Product, on_delete=models.PROTECT)

