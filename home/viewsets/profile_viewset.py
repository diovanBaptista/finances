from home.models import Profile
from home.serializers import ProfileSerializer
from novadata_utils.viewsets import NovadataModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime
from accounts.models import Account, Installment, ContaMensais
from django.db.models import Sum
from django.db.models.functions import ExtractMonth
from entradas.models import Entrada



class ProfileViewSet(NovadataModelViewSet):
    queryset = Profile.objects.all()

    serializer_class = ProfileSerializer
    permission_classes = []

    search_fields = []


    @action(detail=True, methods=['GET'])
    def dashboard(self, request, pk=None):
        now = datetime.now()
        mes_atual = now.month
        ano_atual = now.year

        entradas = Entrada.objects.filter(
            usuario=2,
            data__month=mes_atual,
            data__year=ano_atual
        )

        contas = Account.objects.filter(
            owner_id=2
        )

        contas_unitarias = ContaMensais.objects.filter(
            owner_id=2,
            data__month=mes_atual,
            data__year=ano_atual
        )

        valor_entrada_mensal = entradas.aggregate(total=Sum('valor'))['total'] or 0

        # valor total conta mensal

        valor_conta_mensal = Installment.objects.filter(
            accounts__in=contas,
            maturity__month=mes_atual,
            maturity__year=ano_atual
        ).aggregate(total=Sum('installment_value'))['total'] or 0

        valor_conta_mensal += contas_unitarias.aggregate(total=Sum('valor'))['total'] or 0

        # valor conta mensal Paga

        valor_conta_mensal_paga = Installment.objects.filter(
            accounts__in=contas,
            status='Pago',
            maturity__month=mes_atual,
            maturity__year=ano_atual
        ).aggregate(total=Sum('installment_value'))['total'] or 0

        valor_conta_mensal_paga += contas_unitarias.filter(status='Pago').aggregate(total=Sum('valor'))['total'] or 0


        # valor conta mensal não Paga

        valor_conta_mensal_falta_pagar = Installment.objects.filter(
            accounts__in=contas,
            status='Nao Pago',
            maturity__month=mes_atual,
            maturity__year=ano_atual
        ).aggregate(total=Sum('installment_value'))['total'] or 0

        valor_conta_mensal_falta_pagar +=  contas_unitarias.filter(status='Nao Pago').aggregate(total=Sum('valor'))['total'] or 0

        return Response({
            'valor_conta_mensal': valor_conta_mensal,
            'valor_conta_mensal_pago': valor_conta_mensal_paga,
            'valor_conta_mensal_falta_pagar': valor_conta_mensal_falta_pagar,
            'valor_entradas_mensal': valor_entrada_mensal,
            })
    
    @action(detail=True, methods=['GET'])
    def grafico_contas(self, request, pk=None):
        ano_atual = datetime.now().year

        contas_mensais = Installment.objects.filter(
            accounts__owner_id=2,
            accounts__date__year=ano_atual
        ).annotate(
            mes=ExtractMonth('maturity')
        ).values('mes').annotate(
            total=Sum('installment_value')
        )


        contas_account = ContaMensais.objects.filter(
            owner_id=2,
            data__year=ano_atual
        ).annotate(
            mes=ExtractMonth('data')
        ).values('mes').annotate(
            total=Sum('valor')
        )

        meses_nomes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
                    'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

        resultado = []

        for i in range(1, 13):
            total_mensal = next((item['total'] for item in contas_mensais if item['mes'] == i), 0) or 0
            total_account = next((item['total'] for item in contas_account if item['mes'] == i), 0) or 0
            total_geral = total_mensal + total_account

            resultado.append({
                'mes': meses_nomes[i - 1],
                'total': total_geral,
                'conta_mensal': total_mensal,
                'conta_account': total_account
            })

        return Response(resultado)
        
    @action(detail=True, methods=['GET'])
    def grafico_entradas(self, request, pk=None):
        ano_atual = datetime.now().year

        # Entradas
        entradas = Entrada.objects.filter(
            usuario=2,
            data__year=ano_atual
        ).annotate(
            mes=ExtractMonth('data')
        ).values('mes').annotate(
            total=Sum('valor')
        )


        meses_nomes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
                       'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

        resultado = []
        for i in range(1, 13):
            # Total de entradas
            total_entradas = next((item['total'] for item in entradas if item['mes'] == i), 0) or 0

            resultado.append({
                'mes': meses_nomes[i - 1],
                'entradas': total_entradas,
            })

        return Response(resultado)
