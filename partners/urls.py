from django.urls import path
from partners.views import partners

urlpatterns = [
    path('', partners, name="partners")
]
