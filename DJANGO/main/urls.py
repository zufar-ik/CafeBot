from django.urls import path, include

from .views import UsersAdd, ProductAdd

urlpatterns = [
    path('user/',UsersAdd.as_view()),
    path('product/',ProductAdd.as_view())
]