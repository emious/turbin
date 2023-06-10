from django.urls import path
from product.views import product_category, product_list

urlpatterns = [
    path('', product_category),
    path('list/<int:id>', product_list)
]
