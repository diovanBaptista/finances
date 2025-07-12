from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from ...models import TipoConta
from ..serializers import TipoContaSerializer


class TipoContaViewSet(viewsets.ModelViewSet):
    queryset = TipoConta.objects.all()
    serializer_class = TipoContaSerializer
    permission_classes = []

    filter_backends = [filters.SearchFilter]

    search_fields = [
        
    ]
