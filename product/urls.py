from django.urls import path
from product.views import product_category, product_list, product_detail

urlpatterns = [
    path('', product_category, name="product_category"),
    path('list/<int:id>', product_list, name="product_list"),
    path('detail<int:id>', product_detail, name="product_detail")

]
