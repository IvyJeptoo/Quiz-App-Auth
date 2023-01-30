from rest_framework.permissions import BasePermission


class IsStudentUser(BasePermission):
    # defines who is able to access a particular view
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_student)


class IsTeacherUser(BasePermission):
    # defines who is able to access a particular view
    def has_permission(self, request, view):
        
        return bool(request.user and request.user.is_teacher)