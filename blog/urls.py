from django.urls import path
from blog.views import blog, detail_blog
urlpatterns = [
    path('', blog),
    path('content/<int:id>', detail_blog, name="detail_blog")
]
