from django import forms
from core.models import Product, Seller, Marketplace, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': "Nome",
            'categories': "Categories",
            'description': "Descrição",
        }

    labels = {
        'name': "Nome",
        'categories': "Categories",
        'price': "Preço",
        'description': "Descrição",
    }


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'

        widgets = {
            'fantasy_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'Address': forms.TextInput(attrs={'class': 'form-control'}),

            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'fantasy_name': "Nome Fantasia",
            'company_name': "Razão social",
            'cnpj': "CNPJ",
            'contact_email': "E-amail",
            'contact_phone': "Telefone",
            'Address': "Endereço",
            'city': "Cidade",
            'state': "Estado",
            'district': "Bairro",
            'zipcode': "CEP",
        }


class MarketplaceForm(forms.ModelForm):
    class Meta:
        model = Marketplace
        fields = '__all__'

        widgets = {
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'technical_manager': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'website': "Site",
            'contact_email': "E-mail",
            'contact_phone': "Telefone",
            'name': "Nome",
            'description': "Descrição",
            'technical_manager': "Responsável técnico",
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': "Nome",
            'categories': "Categories",
            'description': "Descrição",
        }

    labels = {
        'name': "Nome",
        'categories': "Categories",
        'description': "Descrição",
    }
