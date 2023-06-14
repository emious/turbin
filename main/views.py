from django.shortcuts import render
from django.template import RequestContext

from product.models import Category
from blog.models import Content
from main.models import Slider
from partners.models import Partner


# Create your views here.

def index_page(reqeust):
    categories = Category.objects.all()
    partners = Partner.objects.filter().reverse().order_by('-id')[0:3]
    blog_content = Content.objects.filter().order_by('-id')[:10]
    slider = Slider.objects.all()

    context = {'Category': categories,
               'Blog': blog_content,
               'Slider': slider,
               "Partners": partners

               }
    return render(reqeust, 'main/index.html', context)


def about_us_page(request):

    return render(request, 'main/about.html')


def contact_page(request):

    return render(request, 'main/contact.html')


def error_404(request, exception):
    return render(request, 'main/error.html')