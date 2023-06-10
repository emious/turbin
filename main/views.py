from django.shortcuts import render
from product.models import Category
from blog.models import Content
from main.models import Slider


# Create your views here.

def index_page(reqeust):
    categories = Category.objects.all()
    blog_content = Content.objects.filter().order_by('-id')[:10]
    slider = Slider.objects.all()

    context = {'Category': categories,
               'Blog': blog_content,
               'Slider': slider

               }
    return render(reqeust, 'main/index.html', context)
