from django.urls import path

from core.views import home, product_update, seller_create, \
    seller_list, seller_update, seller_delete, marketplace_create, marketplace_list, \
    product_delete, product_list, product_create, marketplace_delete, marketplace_update, category_list, \
    category_update, category_create, category_delete

urlpatterns = [
    path('', home, name='home'),
    path('list/products/', product_list, name='products'),
    path('post/proucts/', product_create, name='new-product'),
    path('update/product/<int:pk>', product_update, name='update-product'),
    path('delete/product/<int:pk>/remove', product_delete, name='delete-product'),

    path('seller/create/', seller_create, name='seller-create'),
    path('seller/list/', seller_list, name='seller-list'),
    path('seller/update/<int:pk>', seller_update, name='seller-update'),
    path('seller/delete/<int:pk>/remove', seller_delete, name='seller-delete'),

    path('marketplace/create/', marketplace_create, name='marketplace-create'),
    path('marketplace/list/', marketplace_list, name='marketplace-list'),
    path('marketplace/update/<int:pk>', marketplace_update, name='marketplace-update'),
    path('marketplace/delete/<int:pk>/remove', marketplace_delete, name='marketplace-delete'),

    path('category/list/', category_list, name='category-list'),
    path('category/update/<int:pk>', category_update, name='category-update'),
    path('category/delete/<int:pk>', category_delete, name='category-delete'),
    path('category/create/', category_create, name='category-create'),

]
