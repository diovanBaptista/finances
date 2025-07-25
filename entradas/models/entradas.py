from django.db import models


class Entrada(models.Model):

    tipo_entrada = models.ForeignKey(
        'entradas.TipoEntrada',
        on_delete=models.DO_NOTHING,
        verbose_name='Tipo Entrada',
    )

    usuario = models.ForeignKey(
        'home.Profile',
        on_delete=models.DO_NOTHING,
        verbose_name='Usuario'
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

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return f"{self.id}"

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'entradas'
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
