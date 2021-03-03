from django.urls import path

from core.views import home, myProductsView, productNewView

urlpatterns = [
    path('', home, name='home'),
    path('list/products/', myProductsView.as_view(), name='products'),
    path('post/proucts/', productNewView.as_view(),  name='new-product')


]
