from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer
from .permissions import UserModifyPermission


class UserViewset(ModelViewSet):

    serializer_class = UserSerializer
    permission_classes = [UserModifyPermission]

    def get_queryset(self):
        return User.objects.all()
