# Generated by Django 3.2.12 on 2023-10-03 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição da sua compra')),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor total da Conta')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Data da Compra')),
                ('installments', models.BooleanField(default=False, verbose_name=' Essa conta é Parcelada?')),
                ('installment_number', models.IntegerField(blank=True, max_length=5, null=True, verbose_name='Nuúmero de Parcelas')),
                ('store', models.CharField(blank=True, max_length=100, null=True, verbose_name='Loja onde foi comprado')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
    ]
