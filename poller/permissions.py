from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        print(user.is_staff)

        if user.is_staff:
            return True

        if user.is_superuser:
            return True

        if request.method in ("HEAD", "GET"):
            return True

        return False
