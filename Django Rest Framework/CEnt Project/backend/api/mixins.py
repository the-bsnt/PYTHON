from rest_framework import permissions
from .permission import *


class StaffEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


class UserQuerySetMixin:
    user_field = "user"

    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        # if self.request.user.is_staff:
        #     return qs

        return qs.filter(**lookup_data)
