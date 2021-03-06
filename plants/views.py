from rest_framework import viewsets

from .serializers import PictureSerializer
from .models import Picture


class PictureViewSet(viewsets.ModelViewSet):
    serializer_class = PictureSerializer
    queryset = Picture.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
