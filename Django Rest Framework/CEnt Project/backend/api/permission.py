from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        usr = request.user
        if usr.is_staff:
            if request.method == "GET":
                return usr.has_perm("products.view_product")
            return True
        return super().has_permission(request, view)
