from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class BaseModel(models.Model):
    name = models.CharField('Nome', max_length=150)
    description = models.CharField('Descrição', max_length=255)

    class Meta:
        abstract = True


class Category(BaseModel):
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-list')


class Product(BaseModel):
    categories = models.ManyToManyField(Category, related_name='categories')
    prince = models.DecimalField(max_length=8, decimal_places=2, max_digits=30)

    class Meta:
        verbose_name_plural = "Products"
        verbose_name = 'Product'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products')


class Marketplace(BaseModel):
    contact_phone = models.CharField('Telefone', max_length=14)
    contact_email = models.EmailField('E-mail', max_length=120)
    website = models.URLField('website', blank=True)
    technical_manager = models.CharField('Responsável técnico', max_length=255)

    def get_absolute_url(self):
        return reverse('marketplace-list')

    class Meta:
        verbose_name_plural = 'Marketplaces'
        verbose_name = 'Marketplace'

    def __str__(self):
        return self.name


class Seller(models.Model):
    fantasy_name = models.CharField('Nome Fantasia', max_length=150)
    company_name = models.CharField('Razão Social', max_length=250)
    cnpj = models.CharField('CNPJ', max_length=18)
    contact_email = models.EmailField('E-mail', max_length=120)
    contact_phone = models.CharField('Telefone', max_length=14)
    street = models.CharField('Rua', max_length=220)
    zipcode = models.CharField('Cep', max_length=9)
    number = models.CharField('Numero', max_length=4)
    district = models.CharField('Bairro', max_length=170)
    uf = models.CharField('UF', max_length=3)
    city = models.CharField('Cidade', max_length=120)
    products = models.ManyToManyField(Product, related_name='products')

    class Meta:
        verbose_name_plural = 'sellers'
        verbose_name = 'Seller'

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return 'saller_list'
