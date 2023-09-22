from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # form = UserChangeForm
    # add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["email", "mobile_number", "is_staff", "role"]
    list_filter = ["is_staff"]
    # fieldsets = [
    #     (None, {"fields": ["email", "password"]}),
    #     ("Personal info", {"fields": ["date_of_birth"]}),
    #     ("Permissions", {"fields": ["is_admin"]}),
    # ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    # add_fieldsets = [
    #     (
    #         None,
    #         {
    #             "classes": ["wide"],
    #             "fields": ["email", "date_of_birth", "password1", "password2"],
    #         },
    #     ),
    # ]
    search_fields = ["email", "mobile_number"]
    ordering = ["mobile_number"]
    filter_horizontal = []
