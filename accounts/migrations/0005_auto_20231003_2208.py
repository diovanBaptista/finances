# Generated by Django 3.2.12 on 2023-10-03 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_account_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='installment_number',
            field=models.IntegerField(blank=True, max_length=5, null=True, verbose_name='Número de parcelas'),
        ),
        migrations.AlterField(
            model_name='account',
            name='installments',
            field=models.BooleanField(default=False, verbose_name=' Essa conta é parcelada'),
        ),
    ]
