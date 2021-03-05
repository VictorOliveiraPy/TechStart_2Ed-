from django.test import TestCase

from core.models import Product


class TestProductModelTest(TestCase):
    def setUp(self):
        self.obj = Product(
            name='Notebook',
            description='i5 2020',
            prince='124',
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Product.objects.exists())  # Verificar se existe no banco de dados

    def test_str(self):
        self.assertEqual('Notebook', str(self.obj))




