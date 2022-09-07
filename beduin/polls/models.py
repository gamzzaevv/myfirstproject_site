from django.db import models

class ProductType(models.Model):
    prosto_product_type = models.CharField(max_length=150, verbose_name="Тип продукта")

class Delivery(models.Model):
    product_name = models.CharField(max_length=180, verbose_name="Название продукта")
    product_type = models.ManyToManyField(ProductType, verbose_name="Тип продукта", related_name='tags')
    delivery_date = models.DateField(verbose_name="Дата доставки")
    file_attachment = models.FileField(verbose_name="Файл-аттачмент")

class MoreAddress(models.Model):
    address = models.TextField(verbose_name="Адреса")
    Many_address = models.ForeignKey(Delivery, on_delete=models.CASCADE, verbose_name="Множественные адреса")
