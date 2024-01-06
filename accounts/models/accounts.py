from django.db import models


class Account(models.Model):

    STATUS_CHOICES = (
        ('Parte cadastro', 'Parte cadastro'),
        ('Parte financeira', 'Parte financeira'),
        ('Parte completada', 'Parte completada'),
    )

    status = models.CharField(
        verbose_name='Status',
        max_length=50,
        choices=STATUS_CHOICES,
        default='Parte cadastro',
        null=True,blank=True
    )

    name = models.CharField(
        verbose_name='Nome',
        max_length=100,
        null=True,blank=True
    )

    description = models.TextField(
        verbose_name="Descrição",
        null=True,blank=True
    )

    value = models.DecimalField(
        verbose_name='Valor total',
        max_digits=10,
        decimal_places=2,
        null=True,blank=True
    )

    date = models.DateField(
        verbose_name="Data",
        blank=True,null=True
    )

    installments = models.BooleanField(
        verbose_name=" Essa conta é parcelada",
        default=False
    )

    due_date_day =  models.CharField(
        verbose_name='Dia vencimento',
        max_length=100,
        null=True,blank=True
    )

    installment_number = models.IntegerField(
        verbose_name="Número de parcelas",
        null=True,blank=True
    )

    store = models.CharField(
        verbose_name='Loja',
        max_length=100,
        null=True,blank=True
    )


    def pode_avanca_financeiro(self):
        self.status = 'Parte financeira'
        self.save()

    def pode_finalizar(self):
        self.status = 'Parte completada'
        self.save()

    def avancar(self, request):
        if self.status == "Parte cadastro":
            self.pode_avanca_financeiro()
        elif self.status == "Parte financeira":
            self.pode_finalizar()
        else: 
            pass


    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return self.name

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'accounts'
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
