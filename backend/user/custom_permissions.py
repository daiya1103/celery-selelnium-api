from rest_framework import permissions


class UserCreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class UserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id


class KeywordPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.recipe.user.id == request.user.id
