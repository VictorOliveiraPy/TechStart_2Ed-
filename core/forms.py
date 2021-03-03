from django.core.validators import RegexValidator
from django import forms

# class RegistrationForm(forms.Form):
#     only_number = RegexValidator(r'^[0-9]*$', 'Caracter não numérico no campo telefone, por favor verifique novamente')
#
#     fantasy_name = forms.CharField('Nome Fantasia', max_length=255)
#     company_name = forms.CharField('Razão Social', max_length=255)
#     cnpj = forms.CharField('CNPJ', max_length=26)
#     contact_email = forms.EmailField('E-mail', max_length=255)
#     Contact_phone = forms.CharField('Telefone', max_length=14, validators=[only_number])
#     Street = forms.CharField('Rua', max_length=150)
#     Zipcode = forms.CharField('CEP', max_length=20)
#     number = forms.CharField('Numero', max_length=14)
#     district = forms.CharField('Bairro', max_length=16)
#     city = forms.CharField('Cidade', max_length=100)
from core.models import Product


class ProductFormOld(forms.Form):
    name = forms.CharField(label='Nome', max_length=200, required=True)
    quantity = forms.CharField(label='Quantidade', max_length=5, required=True)
    prince = forms.CharField(label='Valor', max_length=200, required=True)
    description = forms.CharField(label='Descrição', max_length=200, required=True, widget=forms.Textarea)
    categories = forms.CharField(label='Categori', max_length=200, required=True)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'prince', 'description', 'categories']
