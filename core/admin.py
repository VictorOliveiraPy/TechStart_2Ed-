from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from django.contrib import admin

from core.models import Category, Product, Seller, Marketplace


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MarketplaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_phone', 'contact_email', 'website')


class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'fantasy_name', 'company_name')


admin.site.register(Seller, SellerAdmin)
admin.site.register(Marketplace, MarketplaceAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductsAdmin)
