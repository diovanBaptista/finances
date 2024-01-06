import json
from django.http import JsonResponse
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
import django_filters.rest_framework
from ...models import Installment
from ..serializers import InstallmentSerializer
from rest_framework.decorators import action

class InstallmentViewSet(viewsets.ModelViewSet):
    queryset = Installment.objects.all()
    serializer_class = InstallmentSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        filters.SearchFilter,
        django_filters.rest_framework.DjangoFilterBackend,
    ]

    filterset_fields = ['status','accounts']
    search_fields = [
        
    ]


    
    @action(detail=True,methods=["GET"])
    def parcela_paga(self, request, pk=None):
        parcela = Installment.objects.get(id=pk)
        if parcela.status == 'Nao Pago':
            parcela.status = 'Pago'
            parcela.save()
            return JsonResponse({"message":f"Parcela {parcela} foi paga, pagamento foi no valor de {parcela.installment_value} "})
        else:
            return JsonResponse({"error":"Parcela nao encontrada"})


    def get_queryset(self):
        query =  super().get_queryset()
        month = self.request.query_params.get('month', None)
        year = self.request.query_params.get('year', None)
        
        if month:
            query = query.filter(maturity__month=month)

        if year:
            query = query.filter(maturity__year=year)
    
        return query

