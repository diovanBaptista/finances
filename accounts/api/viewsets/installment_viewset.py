import re
from django.http import JsonResponse
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
import django_filters.rest_framework
from ...models import Installment
from ..serializers import InstallmentSerializer
from rest_framework.decorators import action
from django.db.models import Sum
from rest_framework.pagination import PageNumberPagination

class InstallmentPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class InstallmentViewSet(viewsets.ModelViewSet):
    queryset = Installment.objects.all()
    serializer_class = InstallmentSerializer
    pagination_class = (InstallmentPagination)
    permission_classes = []
    # permission_classes = [IsAuthenticated]

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
        
    
    # @action(detail=False, methods=["GET"])
    # def dados_mensais(self,request):
    #     month = self.request.query_params.get('month', None)
    #     year = self.request.query_params.get('year', None)
    #     parcelas = Installment.objects.all()
    #     if month:
    #         parcelas = parcelas.filter(maturity__month=month)
    #     if year:
    #         parcelas = parcelas.filter(maturity__year=year)

    #     dados_mensais = []
    #     n_parcelas_pagas = parcelas.filter(status="Pago").count()
    #     n_parcelas_nao_pagas = parcelas.filter(status="Nao Pago").count()
    #     parcelas_paga = 0
    #     parcelas_nao_paga = 0
    #     for parcela in parcelas:
    #         if parcela.status == "Pago":
    #             parcelas_paga += parcela.installment_value
    #         if parcela.status == "Nao Pago":
    #             parcelas_nao_paga += parcela.installment_value
    #         dados_mensais.append({
    #             "parcelas_pagas":n_parcelas_pagas,
    #             "parcelas_nao_pagas":n_parcelas_nao_pagas,
    #             "valor_pago":parcelas_paga,
    #             "valor_nao_pago":parcelas_nao_paga,
    #         })
    #     return JsonResponse(dados_mensais)
        
    @action(detail=False, methods=["GET"])
    def trazer_todos_os_anos(self, request):
        parcelas = Installment.objects.all()

        anos = parcelas.order_by('maturity__year').values_list('maturity__year', flat=True).distinct()

        if not anos:
            return JsonResponse({"error": "Nenhum ano encontrado para as parcelas."}, safe=False)

        return JsonResponse({"anos": list(anos)}, safe=False)

    
    @action(detail=False, methods=["GET"])
    def dados_mensais(self, request):
        month = self.request.query_params.get('month', None)
        year = self.request.query_params.get('year', None)
        parcelas = Installment.objects.all()
        
        if not month:
            return JsonResponse({"error":"Filtro de mes e ano não preenchidos"})
        if month:
            parcelas = parcelas.filter(maturity__month=month)
        if year:
            parcelas = parcelas.filter(maturity__year=year)

        n_parcelas_pagas = parcelas.filter(status="Pago").count()
        n_parcelas_nao_pagas = parcelas.filter(status="Nao Pago").count()

        dados_mensais = {
            "mes": month,
            "ano": year,
            "parcelas_pagas": n_parcelas_pagas,
            "parcelas_nao_pagas": n_parcelas_nao_pagas,
        }

        valores_parcelas = parcelas.values('status').annotate(Sum('installment_value'))

        for valor_parcela in valores_parcelas:
            status = valor_parcela['status']
            valor = valor_parcela['installment_value__sum']

            if status == "Pago":
                dados_mensais["valor_pago"] = round(valor,2)
            elif status == "Nao Pago":
                dados_mensais["valor_nao_pago"] = round(valor,2)

        return JsonResponse(dados_mensais, safe=False)

    def get_queryset(self):
        query =  super().get_queryset()
        month = self.request.query_params.get('month', None)
        year = self.request.query_params.get('year', None)
        
        if month:
            query = query.filter(maturity__month=month)

        if year:
            query = query.filter(maturity__year=year)
    
        return query

