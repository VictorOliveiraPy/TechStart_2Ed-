from django.test import TestCase

from core.models import Category


class TestCategoryModelTest(TestCase):
    def setUp(self):
        self.obj = Category(
            name='Eletronicos',
            description='equipamentos de informatica',

        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Category.objects.exists())

    def test_str(self):
        self.assertEqual('Eletronicos', str(self.obj))
