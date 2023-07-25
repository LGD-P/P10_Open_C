from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerialiser


class UserViewset(ModelViewSet):

    serializer_class = UserSerialiser

    def get_queryset(self):
        return User.objects.all()

    def perform_create(self, serializer_class):
        instance = serializer_class.save()
        instance.user_under_15()
