from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import Account, Installment


@receiver(post_save, sender=Account)
def calcular_valor_parcela(sender, instance, **kwargs):
    if instance.status == 'Parte financeira':
        if instance.installment_number:
            parcelas = instance.installment_number
            count = 0
            for numero in range(1, parcelas + 1):
                installment = Installment.objects.create(accounts=instance)
                count += 1
                installment.calcular_valor_parcela()
                installment.calculardata_vencimento(instance,count)



            
# @receiver(post_save, sender=Account)
# def calcular_ja_pago(sender, instance, **kwargs):
#     if instance.status == 'Parte completada':
#         installments = Installment.objects.filter(accounts=instance)
#         for installment in installments:
#             installment.calcular_ja_pago()
            