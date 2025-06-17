from django.db import models
from .accounts import Account
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import calendar



class Installment(models.Model):

    STATUS_CHOICES = (
        ('Pago', 'Pago'),
        ('Nao Pago', 'Nao Pago'),
    )

    status = models.CharField(
        verbose_name='Status',
        max_length=50,
        choices=STATUS_CHOICES,
        default='Nao Pago',
        null=True,blank=True
    )

    accounts = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name='conta',
        blank=True,null=True,
    )

    installment_value = models.DecimalField(
        verbose_name='Valor parcelas',
        max_digits=10,
        decimal_places=2,
        null=True,blank=True
    )

    maturity = models.DateField(
        verbose_name="Vencimento da Parcela",
        blank=True,null=True
    )

    def calcular_valor_parcela(self):
        if self.accounts.installments == True:
            self.installment_value =  self.accounts.value / self.accounts.installment_number
            self.save()
        else: 
            return None
        

    def calculardata_vencimento(self, instance, count):
        if instance:
            data_compra = self.accounts.date  # já é um DateField, não precisa strptime
            dia = int(instance.due_date_day)

            # Garante que o dia seja válido para o mês da data original
            ultimo_dia_mes = calendar.monthrange(data_compra.year, data_compra.month)[1]
            dia = min(dia, ultimo_dia_mes)

            data_base = data_compra.replace(day=dia)
            data_pagamento = data_base + relativedelta(months=count)

            # Corrige o dia se o novo mês não tiver o dia desejado
            ultimo_dia_novo_mes = calendar.monthrange(data_pagamento.year, data_pagamento.month)[1]
            dia = min(int(instance.due_date_day), ultimo_dia_novo_mes)
            data_pagamento = data_pagamento.replace(day=dia)

            self.maturity = data_pagamento
            self.save()

    # def calcular_ja_pago(self):
    #     if self.accounts:
    #         hoje = datetime.now()
    #         data_compra = self.accounts.date
    #         diferenca = (hoje.year - data_compra.year) * 12 + (hoje.month - data_compra.month)
    #         self.amount_paid = self.installment_value * diferenca

    #         data_compra = f"{self.accounts.date}"
    #         data_compra = datetime.strptime(data_compra, '%Y-%m-%d')
    #         num_parcelas = self.accounts.installment_number
    #         data_pagamento = data_compra + relativedelta(months=num_parcelas)
            
    #         mes_pagamento = data_pagamento.month
    #         mes_pagamento = calendar.month_name[mes_pagamento]
    #         ano_pagamento = data_pagamento.year
    #         self.month_year = f"{mes_pagamento}/{ano_pagamento}"
    #         self.save()
    #         return diferenca

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return f"{self.id}"

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'accounts'
        verbose_name = 'Parcela'
        verbose_name_plural = 'Parcelas'
