from django.shortcuts import render
from product.models import Category


# Create your views here.

def index_page(reqeust):
    categories = Category.objects.all()
    context = {'Category': categories}
    return render(reqeust, 'main/index.html', context)
