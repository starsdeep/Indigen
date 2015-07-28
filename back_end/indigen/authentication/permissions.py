__author__ = 'fucus'
from rest_framework import permissions


class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, account):
        if request.user:
            return account == request.user
        return False


class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, account):
        return self.has_permission(request,view)


    def has_permission(self, request, view):
        try:
            return request.user.is_admin
        except AttributeError:
            return False