from home.models import Profile
from home.serializers import ProfileSerializer
from novadata_utils.viewsets import NovadataModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime
from accounts.models import Account, Installment, ContaMensais
from django.db.models import Sum



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

        contas = Account.objects.filter(
            owner_id=2
        )

        contas_unitarias = ContaMensais.objects.filter(
            owner_id=2,
            data__month=mes_atual,
            data__year=ano_atual
        )

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
            'valor_conta_mensal_falta_pagar': valor_conta_mensal_falta_pagar
            })

