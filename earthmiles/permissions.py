__author__ = 'som'

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only owners of an object to edit it
    """

    def has_object_permission(self, request, view, obj):
        """
        Read permissions are allowed to any request
        So we will always allow GET, HEAD or OPTIONS as these are safe methods
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        #write permissions are only allowed to object owner
        if obj.owner == request.user:
            print 
            return True
        else:
            return False
