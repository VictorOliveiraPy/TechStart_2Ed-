from ajax_select import register, LookupChannel
from django.contrib.auth.models import User

from core.models import Category


@register('user')
class UserLook(LookupChannel):
    model = User

    def get_query(self, q, request):
        return self.model.objects.filter(username__icontains=q).order_by('username') # List user


@register('categories')
class CategoryLook(LookupChannel):
    model = Category

    def get_query(self, q, request):
        return self.model.objects.filter(name__icontains=q).order_by('name')
