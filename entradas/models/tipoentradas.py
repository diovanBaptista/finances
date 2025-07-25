from django.db import models


class TipoEntrada(models.Model):

    nome = models.CharField(
        verbose_name='Nome',
        max_length=100,
    )

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return self.nome

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'entradas'
        verbose_name = 'Tipo Entrada'
        verbose_name_plural = 'Tipos Entradas'
