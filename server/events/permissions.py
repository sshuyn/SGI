from rest_framework import permissions

class IsUserAuthenticated(permissions.BasePermission):
  message = "You are not allowed."
  
  def has_object_permission(self, request, view, obj):
    return obj.user == request.user