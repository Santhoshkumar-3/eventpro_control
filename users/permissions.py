from rest_framework import permissions

class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only staff members to create, update, and delete events.
    """

    def has_permission(self, request, view):
        # Allow read-only permissions for non-staff users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is authenticated and has the 'staff' role
        return request.user.is_authenticated and request.user.role == 'staff'
