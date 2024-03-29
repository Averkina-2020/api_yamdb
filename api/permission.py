from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_role_admin
        )


class IsAuthenticatedOrAdmin(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return super(IsAuthenticated, self).has_permission(request, view)


class IsAuthorModeratorAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and (
                obj.author == request.user
                or request.user.is_moderator
                or request.user.is_admin
            )
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and (
                request.user.is_staff
                or request.user.is_role_admin
            )
        )


class IsAuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.method == 'DELETE'
            and (request.user.is_role_admin or request.user.is_role_moderator)
        )
