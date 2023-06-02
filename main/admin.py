from django.contrib import admin

# Register your models here.
from main import models
from main.models import WebsiteSetting


@admin.register(WebsiteSetting)
class WebsiteSetting(admin.ModelAdmin):
    list_display = ("phone_number",)



    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

    def has_add_permission(self, request):
        return False



