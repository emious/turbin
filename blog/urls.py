from django.urls import path
from blog.views import myview
urlpatterns = [
    path('', myview)
]
