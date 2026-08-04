from rest_framework.viewsets import ModelViewSet

from core.models import Compra
from core.serializers import CompraSerializer, CompraUpdateCreateSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def get_serializer_class(self):
        if self.action in {'create', 'update', 'partial_update'}:
            return CompraUpdateCreateSerializer
        return super().get_serializer_class()
