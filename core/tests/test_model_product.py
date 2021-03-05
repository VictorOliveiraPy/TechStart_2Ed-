from django.test import TestCase

from core.models import Product


class TestProductModelTest(TestCase):
    def setUp(self):
        self.obj = Product(
            name='Notebook',
            description='i5 2020',
            price='124',
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Product.objects.exists())

    def test_str(self):
        self.assertEqual('Notebook', str(self.obj))
