from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import *


@admin.register(User)
class EmployeeAdmin(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('phone_number',)}),
    )

admin.site.register(Banner)
admin.site.register(Support)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Vendors)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Image)
admin.site.register(Blog)
admin.site.register(About)
admin.site.register(Team)
admin.site.register(Information)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Cart)
