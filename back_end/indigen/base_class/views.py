from rest_framework.viewsets import ModelViewSet
from authentication.permissions import IsAdmin
from rest_framework.views import APIView







class BaseModelView(ModelViewSet):
    def check_permissions(self, request):
        """
        Check if the request should be permitted.
        Raises an appropriate exception if the request is not permitted.
        """

        u = IsAdmin()

        if u.has_permission(request,self):
            return True

        for permission in self.get_permissions():
            if not permission.has_permission(request, self):
                self.permission_denied(request)

    def check_object_permissions(self, request, obj):
        """
        Check if the request should be permitted for a given object.
        Raises an appropriate exception if the request is not permitted.
        """
        u = IsAdmin()
        if u.has_object_permission(request,self,obj):
            return True
        for permission in self.get_permissions():
            if not permission.has_object_permission(request, self, obj):
                self.permission_denied(request)

