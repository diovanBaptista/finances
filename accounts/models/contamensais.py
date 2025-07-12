from django.db import models


class ContaMensais(models.Model):

    conta = models.ForeignKey(
        'accounts.TipoConta',
        on_delete=models.DO_NOTHING,
        verbose_name='conta',
    )

    valor = models.DecimalField(
        verbose_name='Valor',
        max_digits=10,
        decimal_places=2,
        null=True,blank=True
    )

    data = models.DateField(
        verbose_name="Data",
        blank=True,null=True
    )

    owner = models.ForeignKey(
        'home.Profile',
        on_delete=models.SET_NULL,
        verbose_name='Proprietário',
        null=True, blank=True
    )


    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return f"{self.id}"

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'accounts'
        verbose_name = 'Conta mensal'
        verbose_name_plural = 'Conta Mensais'
