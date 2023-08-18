from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .permissions import UserPermission


class UserViewset(ModelViewSet):

    serializer_class = UserSerializer
    permission_classes = [UserPermission, IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return User.objects.all()
