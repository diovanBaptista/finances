from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from ...models import Account
from ..serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class AccountPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    pagination_class = (AccountPagination)
    permission_classes = []
    # permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]

    search_fields = [
        
    ]


    @action(detail=True, methods=['GET'])
    def avancar(self, request, pk=None):
        obj = Account.objects.get(id=pk)

        if obj.status == "Parte cadastro":
            obj.pode_avanca_financeiro()
        elif obj.status == "Parte financeira":
            obj.pode_finalizar()

        serializer = AccountSerializer(obj)
        return Response(serializer.data)
        



