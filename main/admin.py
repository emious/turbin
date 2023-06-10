from django.contrib import admin

# Register your models here.
from main import models
from main.models import WebsiteSetting, NavMenu, Slider


class WebsiteSettingAdmin(admin.ModelAdmin):
    list_display = ("phone_number",
                    "email",
                    "address",
                    "work_time",
                    "about",
                    'image_tag')

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(WebsiteSetting, WebsiteSettingAdmin)
admin.site.register(NavMenu)
admin.site.register(Slider)

