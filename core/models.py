from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField('Nome', max_length=150)
    slug = models.SlugField(unique=True)
    order = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, blank=True, related_name='categories')
    quantity = models.IntegerField(default=1)
    prince = models.DecimalField(max_length=8, decimal_places=2, max_digits=30)

    class Meta:
        verbose_name_plural = "Prooducts"

    def __str__(self):
        return self.name

