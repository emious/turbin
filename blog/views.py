from django.http import HttpResponse
from blog.models import Content

from django.shortcuts import render

# Create your views here.

def myview(request):
    content = Content.objects.first()
    return HttpResponse(content.content)