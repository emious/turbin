from django.shortcuts import render
from partners.models import Partner
# Create your views here.


def partners(request):
    partners_list = Partner.objects.all()
    context = {
        "Partners": partners_list
    }

    return render(request, 'main/partners.html', context)
