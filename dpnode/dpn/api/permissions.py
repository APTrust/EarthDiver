"""
    Knowledge is knowing a tomato is a fruit; wisdom is not putting it in a
    fruit salad.
                - Miles Kington
"""

from rest_framework import permissions

from dpn.data.models import UserProfile

class IsNodeUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        profile = UserProfile.objects.get(user=request.user)
        if profile.node == obj.node:
            return True
        return False