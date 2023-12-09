from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from .models import User
from scrape.models import (
    Amazon,
    Mercari,
    Yahoo,
    Rakuma,
    Paypay,
    Recipe,
    Keyword,
    Common,
    Delete,
    Replace,
    Ngword,
    Exclusion,
    DefaultMargin,
    Margin,
)


# Register your models here.
class UserAdmin(BaseUserAdmin):
    ordering = ()
    list_display = ("username",)
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Amazon)
admin.site.register(Mercari)
admin.site.register(Yahoo)
admin.site.register(Rakuma)
admin.site.register(Paypay)
admin.site.register(Recipe)
admin.site.register(Keyword)
admin.site.register(Common)
admin.site.register(Ngword)
admin.site.register(Exclusion)
admin.site.register(Delete)
admin.site.register(Replace)
admin.site.register(DefaultMargin)
admin.site.register(Margin)
