# Generated by Django 4.0.3 on 2022-09-19 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enigmaControl', '0009_alter_controlvisitas_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresupuestoModelo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mesPresupuesto', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarioPresupuesto', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Presupuesto',
                'verbose_name_plural': 'Presupuestos',
            },
        ),
        migrations.CreateModel(
            name='PresupuestoTabla',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cliente', models.CharField(max_length=100)),
                ('razonSocial', models.CharField(max_length=100)),
                ('periodo', models.CharField(max_length=100)),
                ('cantidad', models.BigIntegerField(max_length=100)),
                ('ventasObjetivo', models.BigIntegerField(max_length=100)),
                ('ventasRealizadas', models.BigIntegerField(max_length=100)),
                ('cobranzaObjetivo', models.BigIntegerField(max_length=100)),
                ('cobranzaRealizada', models.BigIntegerField(max_length=100)),
                ('presupuesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presupuesto', to='enigmaControl.presupuestomodelo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarioPresupuestos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Presupuestos',
                'verbose_name_plural': 'Presupuestos',
            },
        ),
    ]
