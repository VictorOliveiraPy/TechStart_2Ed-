from django.core.validators import RegexValidator
from django import forms
from core.models import Product, Seller, Marketplace, Category


class ProductFormOld(forms.Form):
    name = forms.CharField(label='Nome', max_length=200, required=True)
    prince = forms.CharField(label='Valor', max_length=200, required=True)
    description = forms.CharField(label='Descrição', max_length=200, required=True, widget=forms.Textarea)
    categories = forms.CharField(label='Categoria', max_length=200, required=True)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'prince', 'description', 'categories']


class SellerFormOld(forms.Form):
    #only_number = RegexValidator(r'^[0-9]*$', 'Caracter não numérico no campo telefone, por favor verifique novamente')

    fantasy_name = forms.CharField(label='Nome Fantasia', max_length=255)
    company_name = forms.CharField(label='Razão Social', max_length=255)
    cnpj = forms.CharField(label='CNPJ', max_length=26)
    contact_email = forms.EmailField(label='E-mail', max_length=255)
    contact_phone = forms.CharField(label='Telefone', max_length=14)
    street = forms.CharField(label='Rua', max_length=150)
    zipcode = forms.CharField(label='CEP', max_length=20)
    number = forms.CharField(label='Numero', max_length=14)
    district = forms.CharField(label='Bairro', max_length=16)
    city = forms.CharField(label='Cidade', max_length=100)


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'


class MarketplaceFormOld(forms.Form):
    contact_phone = forms.CharField(label='Telefone', max_length=14)
    contact_email = forms.EmailField(label='E-mail', max_length=120)
    website = forms.URLField(label='website')
    name = forms.CharField(label='Nome', max_length=150)
    description = forms.CharField(label='Descrição', max_length=255)


class MarketplaceForm(forms.ModelForm):
    class Meta:
        model = Marketplace
        fields = '__all__'


class CategoryFormOld(forms.Form):
    name = forms.CharField(label='Nome', max_length=150)
    description = forms.CharField(label='Descrição', max_length=255)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
