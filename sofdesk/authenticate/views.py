from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer
from .permissions import UserModifyPermission

from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import IsAuthenticated


class UserViewset(ModelViewSet):

    serializer_class = UserSerializer
    permission_classes = [UserModifyPermission, IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return User.objects.all()
