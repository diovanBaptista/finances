# Generated by Django 3.2.12 on 2023-10-06 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_account_due_date_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='due_date_day',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Dia vencimento'),
        ),
    ]