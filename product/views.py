from django.shortcuts import render
from product.models import Category, Product
# Create your views here.


def product_category(request):
    category = Category.objects.all()
    context = {
        "category": category,
    }

    return render(request, 'main/services.html', context)


def product_list(request, id):
    product_list = Product.objects.filter(category_id=id)
    context = {
        "product_list": product_list,
    }

    return render(request, 'main/product-list.html', context)

