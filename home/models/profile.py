from django.contrib.auth import get_user_model
from django.db import models
from accounts.models import Account, Installment
from datetime import datetime


class Profile(models.Model):
    User = get_user_model()
    """
    A classe Profile serve para armazernar
    os(as) profiles do sistema.

    Além de fazer as implementações relacionadas
    a um único objeto do tipo Profile.
    """

    usuario = models.OneToOneField(
        User,
        verbose_name="Usuário",
        on_delete=models.CASCADE,
    )


    @property
    def accounts_month(self):
        mes_atual = datetime.now().month
        contas = Account.objects.filter(owner=self.usuario_id).values_list('id', flat=True)
        # parcelas = Installment.objects.filter(accounts__in=contas, status='Pago').values_list('installment_value', flat=True)
        parcelas = Installment.objects.filter(
            accounts__in=contas,
                               
        ).values_list('installment_value', flat=True)

        return parcelas

    def __str__(self):
        return f"{self.usuario}"

    class Meta:
        app_label = "home"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
