from blog.models import Content

from django.shortcuts import render
from blog.models import Content


# Create your views here.

def blog(request):
    contents = Content.objects.all()

    content = {'contents':contents}
    return render(request, 'main/blog.html', content)


def detail_blog(request, id):
    content = Content.objects.get(pk=id)
    contents = Content.objects.filter().reverse().order_by('-id')[0:5]
    keyword_list = content.tags.split(',')
    context = {
        "content": content,
        "contents": contents,
        "keywords": keyword_list
    }
    return render(request, 'main/blog-single.html', context)

