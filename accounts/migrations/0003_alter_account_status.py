# Generated by Django 3.2.12 on 2023-10-03 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20231003_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='status',
            field=models.CharField(blank=True, choices=[('Parte cadastro', 'Parte cadastro'), ('Parte financeira', 'Parte financeira'), ('Parte completada', 'Parte completada')], default='Parte cadastro', max_length=30, null=True, verbose_name='Status'),
        ),
    ]
