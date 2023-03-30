from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.user == request.user)
    
class IsOwnerUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj == request.user)
    
class IsPostOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.post.user == request.user)
    
class IsChatAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.owner == request.user)