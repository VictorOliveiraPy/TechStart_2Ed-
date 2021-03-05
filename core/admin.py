from django.contrib import admin

from django.utils.html import format_html

from core.models import Category, Product, Seller, Marketplace


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'description')


@admin.register(Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_phone', 'contact_email', 'website', 'name', 'description')

    def website_link(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.website)

    website_link.short_description = 'website'


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'fantasy_name', 'company_name')
