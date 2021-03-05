from django.test import TestCase


# Create your tests here.
from core.admin import ProductsAdmin
from core.models import Product


class ProductModelAdminTest(TestCase):
    def setUp(self):
        Product.objects.create(name='notebook', description='teste',
                                    prince='123', phone='81-998832982')
        self.model_admin = ProductsAdmin(Product, )
