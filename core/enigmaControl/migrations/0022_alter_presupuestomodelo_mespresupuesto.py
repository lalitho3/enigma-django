# Generated by Django 4.0.3 on 2022-09-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enigmaControl', '0021_alter_presupuestotabla_razonsocial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuestomodelo',
            name='mesPresupuesto',
            field=models.CharField(choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')], default='Enero', max_length=100, unique=True),
        ),
    ]