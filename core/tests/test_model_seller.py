from django.test import TestCase

from core.models import Product, Seller


class TestProductModelTest(TestCase):
    def setUp(self):
        self.obj = Seller(
            fantasy_name='olist',
            company_name='olist',
            cnpj='92.579.036/0001-90',
            contact_email='victorblog410@gmail.com',
            contact_phone='81-998832982',
            street='rua nova',
            zipcode='50050250',
            number='36',
            district='boa vista',
            uf='pe',
            city='recife',

        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Seller.objects.exists())  # Verificar se existe no banco de dados

    def test_str(self):
        self.assertEqual('olist', str(self.obj))




