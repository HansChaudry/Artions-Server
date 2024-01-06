from django.contrib import admin
from .models import CustomUser, Follow
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Social Information',
            {
                'fields': (
                    'followers',
                    'following'
                )
            }
        )
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Follow)
