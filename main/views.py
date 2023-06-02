from django.shortcuts import render


# Create your views here.

def index_page(reqeust):
    context = {}
    return render(reqeust, 'main/index.html', context)
