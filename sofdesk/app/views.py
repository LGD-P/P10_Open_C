from rest_framework.viewsets import ModelViewSet

from app.models import Project
from app.serializers import ProjectSerialiser


class ProjectViewset(ModelViewSet):

    serializer_class = ProjectSerialiser

    def get_queryset(self):
        return Project.objects.all()
