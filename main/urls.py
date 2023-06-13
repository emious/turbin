from django.urls import path
from main.views import index_page, about_us_page, contact_page
urlpatterns = [
    path('', index_page, name='main'),
    path('aboutus', about_us_page, name='aboutus'),
    path('contact', contact_page, name='contact'),

]
