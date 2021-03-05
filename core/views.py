from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.forms import ProductForm, MarketplaceForm, CategoryForm, SellerForm
from core.models import Product, Seller, Category, Marketplace


def home(request):
    return render(request, 'base.html')


product_list = ListView.as_view(
    template_name='products/product_list.html',
    model=Product)

product_create = CreateView.as_view(
    template_name='products/product_toadd.html',
    model=Product, form_class=ProductForm)

product_update = UpdateView.as_view(
    template_name='products/update_product.html',
    model=Product, form_class=ProductForm)

product_delete = DeleteView.as_view(
    template_name='products/delete_product.html',
    model=Product)

seller_create = CreateView.as_view(
    template_name='seller/seller_create.html',
    model=Seller, form_class=SellerForm)

seller_update = UpdateView.as_view(
    template_name='seller/update_seller.html',
    model=Seller, form_class=SellerForm)

seller_list = ListView.as_view(
    template_name='seller/list_seller.html',
    model=Seller)

seller_delete = DeleteView.as_view(
    template_name='seller/delete_seller.html',
    model=Seller)

marketplace_list = ListView.as_view(
    template_name='marketplace/marketplace_list.html',
    model=Marketplace)

marketplace_delete = DeleteView.as_view(
    template_name='marketplace/marketplace_delete.html',
    model=Marketplace)

marketplace_update = UpdateView.as_view(
    template_name='marketplace/marketplace_update.html',
    model=Marketplace, form_class=MarketplaceForm)

marketplace_create = CreateView.as_view(
    template_name='marketplace/marketplace_create.html',
    model=Marketplace, form_class=MarketplaceForm)

category_list = ListView.as_view(
    template_name='category/category_list.html',
    model=Category)

category_update = UpdateView.as_view(
    template_name='category/category_update.html',
    model=Category, form_class=CategoryForm)

category_create = CreateView.as_view(
    template_name='category/category_create.html',
    model=Category, form_class=CategoryForm)

category_delete = DeleteView.as_view(
    template_name='category/category_delete.html',
    model=Category)
