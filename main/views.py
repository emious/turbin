from django.shortcuts import render
from django.template import RequestContext

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


def about_us_page(request):

    return render(request, 'main/about.html')


def contact_page(request):

    return render(request, 'main/contact.html')


def error_404(request, exception):
    return render(request, 'main/error.html')