# Generated by Django 4.0.3 on 2022-09-23 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enigmaControl', '0028_remove_presupuestotabla_periodo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presupuestomodelo',
            name='periodoPresupuesto',
        ),
    ]
