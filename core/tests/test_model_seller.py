from django.test import TestCase

from core.models import Seller


class TestProductModelTest(TestCase):
    def setUp(self):
        self.obj = Seller(
            fantasy_name='olist',
            company_name='olist',
            cnpj='92.579.036/0001-90',
            contact_email='victorblog410@gmail.com',
            contact_phone='81-998832982',
            address='rua nova',
            zipcode='50050250',
            number='36',
            district='boa vista',
            state='pe',
            city='recife',

        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Seller.objects.exists())

    def test_str(self):
        self.assertEqual('olist', str(self.obj))
