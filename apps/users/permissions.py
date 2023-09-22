from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.core.exceptions import ImproperlyConfigured, PermissionDenied


class CustomerAccessPermission(permissions.BasePermission):
    message = "Adding customers not allowed."

    # def get_permission_required(self, permission_required):
    #     """
    #     Override this method to override the permission_required attribute.
    #     Must return an iterable.
    #     """
    #     if permission_required is None:
    #         raise ImproperlyConfigured(
    #             "{0} is missing the permission_required attribute. Define {0}.permission_required, or override "
    #             "{0}.get_permission_required().".format(self.__class__.__name__)
    #         )
    #     if isinstance(permission_required, str):
    #         perms = (permission_required,)
    #     else:
    #         perms = permission_required
    #     return perms

    def has_permission(self, request, view):
        req_parm = view.permission_required  # must be an array
        user = request.user
        try:
            parms = user.groups.get(name__in=view.group_permission)
            if parms.permissions.filter(codename__in=req_parm).exists():
                return True
            return False
        except Exception as e:
            return False
