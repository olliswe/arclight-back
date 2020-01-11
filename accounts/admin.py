from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Profile"
    fk_name = "user"


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("id", "email", "admin", "staff")
    list_display_links = ("email",)
    list_filter = ("admin", "staff", "active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("admin", "staff", "active")}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
    search_fields = ("email",)
    ordering = ("id",)
    filter_horizontal = ()


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.site_header = "ArcLight Administrator Panel"
