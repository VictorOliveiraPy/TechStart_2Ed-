from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from django.contrib import admin

from core.models import Category, Product


class CategoryAdmin(AjaxSelectAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('id', 'name')


class ProductsAdmin(AjaxSelectAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('id', 'name')
    #form = make_ajax_form(Product, {
        #'user': 'user'
    #})


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductsAdmin)
