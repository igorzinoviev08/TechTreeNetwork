from rest_framework import permissions


class IsActiveEmployee(permissions.BasePermission):
    """
    Право доступа, которое разрешает доступ только активным сотрудникам.
    """

    def has_permission(self, request, view):
        # Доступ разрешен только активным пользователям
        return request.user and request.user.is_authenticated and request.user.is_active
