from django.db import models


class TipoConta(models.Model):

    nome = models.CharField(
        verbose_name='Nome',
        max_length=100,
    )

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return self.nome

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'accounts'
        verbose_name = 'Tipo Conta'
        verbose_name_plural = 'Tipos Contas'
