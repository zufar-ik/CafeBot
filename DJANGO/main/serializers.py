from rest_framework import serializers

from .models import Users, Product, Category


class UsersSer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('tg_id','username','lname')

class CatSer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ProductSer(serializers.ModelSerializer):
    CAT = CatSer(many=True)
    class Meta:
        model = Product
        fields = '__all__'
        lookup_field = 'slug'
