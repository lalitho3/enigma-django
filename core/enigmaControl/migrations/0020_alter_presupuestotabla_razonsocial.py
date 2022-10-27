# Generated by Django 4.0.3 on 2022-09-20 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enigmaVentas', '0013_alter_mantenimientoclientes_codigopostal_and_more'),
        ('enigmaControl', '0019_presupuestotabla_razonsocial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuestotabla',
            name='razonSocial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='razonSocial', to='enigmaVentas.mantenimientoclientes'),
        ),
    ]
