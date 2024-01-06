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

    @property
    def pagou(self):
        pago = 0
        parcelas = self.installment_set.all()
        for parcela in parcelas:
            if parcela.status == 'Pago':
                pago += parcela.installment_value

        return pago

    @property
    def falta_pagar(self):
        falta_pagar = 0
        parcelas = self.installment_set.all()
        for parcela in parcelas:
            if parcela.status == 'Nao Pago':
                falta_pagar += parcela.installment_value

        return falta_pagar
    
    @property
    def parcelas_paga(self):
        falta_pagar = 0
        parcelas = self.installment_set.all()
        parcelas = parcelas.filter(status="Pago").count()
        return parcelas

    @property
    def parcelas_nao_pagas(self):
        parcelas = self.installment_set.all()
        parcelas = parcelas.filter(status='Nao Pago').count()
        return parcelas
    
    @property
    def ultima_parcela(self):
        parcelas = self.installment_set.all()
        parcelas = parcelas.last()
        data = parcelas.maturity
        return data.strftime('%d / %m / %Y')
        

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
