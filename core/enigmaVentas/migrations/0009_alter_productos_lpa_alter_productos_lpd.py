# Generated by Django 4.0.3 on 2022-05-04 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enigmaVentas', '0008_productos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='lpa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='LPA'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='lpd',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='LPD'),
        ),
    ]
