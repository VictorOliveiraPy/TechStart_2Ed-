from django.test import TestCase

from core.models import Marketplace


class TestMarketplaceModelTest(TestCase):
    def setUp(self):
        self.obj = Marketplace(
            name='olist',
            description='Melhor empresa',
            contact_phone='81-998832982',
            contact_email='victorblog410@gmail.com',
            website='https://google.com.br',
            technical_manager='victor hugo'

        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Marketplace.objects.exists())

    def test_str(self):
        self.assertEqual('olist', str(self.obj))
