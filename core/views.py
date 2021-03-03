from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView, CreateView

from core.forms import ProductForm
from core.models import Product


def home(request):
    return render(request, 'home.html')


class myProductsView(ListView):
    model = Product
    template_name = 'product_list.html'


class productNewView(CreateView):
    model = Product
    template_name = 'product_toadd.html'
    form_class = ProductForm

