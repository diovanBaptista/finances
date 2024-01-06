from rest_framework import serializers

from ...models import Account


class AccountSerializer(serializers.ModelSerializer):
    pagou = serializers.ReadOnlyField()
    falta_pagar = serializers.ReadOnlyField()
    parcelas_paga = serializers.ReadOnlyField()
    parcelas_nao_pagas = serializers.ReadOnlyField()
    ultima_parcela = serializers.ReadOnlyField()
    class Meta:
        model = Account
        fields = '__all__'
