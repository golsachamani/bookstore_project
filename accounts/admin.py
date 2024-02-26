from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUsertCreationForm
class CustomUserAdmin(UserAdmin):
    add_form = CustomUsertCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'age', 'email', 'is_staff']
    fieldsets = UserAdmin.fieldsets + ((None,{'fields': ('age',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None,{'fields': ('age',)}),)
                                       

admin.site.register(CustomUser, CustomUserAdmin)