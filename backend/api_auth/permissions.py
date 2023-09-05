from rest_framework.permissions import AllowAny,IsAdminUser,SAFE_METHODS,BasePermission

#custom permission

class AdminOrReadOnly(IsAdminUser):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            bool(request.user and request.user.is_staff)
       

class  ReviewerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view,obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.user == request.user