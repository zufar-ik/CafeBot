from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Users, Product
from .serializers import UsersSer, ProductSer
from pytils.translit import slugify


class UsersAdd(CreateAPIView):
    queryset =Users.objects.all()
    serializer_class = UsersSer

class ProductAdd(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSer
    def get_context_data(self, **kwargs):
        context = super(ProductAdd, self).get_context_data(**kwargs)
        context['slug'] = slugify(kwargs['title'])
        return context


