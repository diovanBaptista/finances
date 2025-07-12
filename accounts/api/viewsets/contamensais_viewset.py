from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from ...models import ContaMensais
from ..serializers import ContaMensaisSerializer


class ContaMensaisViewSet(viewsets.ModelViewSet):
    queryset = ContaMensais.objects.all()
    serializer_class = ContaMensaisSerializer
    permission_classes = []

    filter_backends = [filters.SearchFilter]

    search_fields = [
        
    ]
