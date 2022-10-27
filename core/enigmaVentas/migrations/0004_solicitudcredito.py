# Generated by Django 4.0.3 on 2022-05-02 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enigmaVentas', '0003_mantenimientoclientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudCredito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('RazonSocial', models.CharField(max_length=200, verbose_name='Razón Social')),
                ('Codigo', models.CharField(blank=True, max_length=150, null=True, verbose_name='Codigo')),
                ('Rfc', models.CharField(max_length=30, verbose_name='RFC')),
                ('NombreComercial', models.CharField(max_length=200, verbose_name='Nombre Comercial')),
                ('CodRuta', models.CharField(blank=True, max_length=200, null=True, verbose_name='Codigo de Ruta')),
                ('CodAgente', models.CharField(blank=True, max_length=200, null=True, verbose_name='Codigo de Agente')),
                ('NombreAgente', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre de Agente')),
                ('DireccionFiscal', models.CharField(max_length=250, verbose_name='Dirección Fiscal')),
                ('NumExt', models.CharField(blank=True, max_length=6, verbose_name='Numero Exterior')),
                ('NumInt', models.CharField(blank=True, max_length=6, verbose_name='Numero Interior')),
                ('Colonia', models.CharField(blank=True, max_length=200, verbose_name='Colonia')),
                ('Estado', models.CharField(blank=True, max_length=100, verbose_name='Estado')),
                ('Municipio', models.CharField(blank=True, max_length=100, verbose_name='Municipio')),
                ('CodigoPostal', models.IntegerField(blank=True, null=True, verbose_name='Código Postal')),
                ('PuntoVenta', models.CharField(max_length=250, verbose_name='Dirección Punto de Venta')),
                ('Telefono', models.PositiveBigIntegerField(verbose_name='Numero Telefonico')),
                ('Fax', models.CharField(blank=True, max_length=200, verbose_name='Fax')),
                ('CorreoElectronico', models.EmailField(max_length=254, null=True, verbose_name='Correo Electronico')),
                ('ListaPrecios', models.CharField(blank=True, choices=[('LPA', 'LPA'), ('LPD', 'LPD')], max_length=250, null=True, verbose_name='Lista de Precios')),
                ('DescuentoGeneral', models.SmallIntegerField(blank=True, null=True, verbose_name='Descuento General (%)')),
                ('Plazo', models.CharField(blank=True, max_length=250, verbose_name='Plazo')),
                ('DescuentosLinea', models.CharField(blank=True, max_length=150, verbose_name='Descuentos especiales por linea')),
                ('LineaCredito', models.CharField(blank=True, max_length=150, null=True, verbose_name='Linea de Crédito')),
                ('Fletera', models.CharField(blank=True, max_length=150, null=True, verbose_name='Fletera')),
                ('ContactoFletera', models.CharField(blank=True, max_length=150, verbose_name='Contacto Fletera')),
                ('DireccionFletera', models.CharField(blank=True, max_length=150, verbose_name='Dirección Fletera')),
                ('TelefonoFletera', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Numero Celular Fletera')),
                ('DescuentoPronto', models.IntegerField(blank=True, null=True, verbose_name='Descuento Pronto Pago (%)')),
                ('InteresMoratorio', models.IntegerField(blank=True, null=True, verbose_name='Interes Moratorio Mensual (%)')),
                ('Gerente', models.CharField(blank=True, max_length=200, null=True, verbose_name='Gerente')),
                ('PersonaCompras', models.CharField(blank=True, max_length=200, null=True, verbose_name='Persona Encargada de Compras')),
                ('PersonaVentas', models.CharField(blank=True, max_length=200, null=True, verbose_name='Persona Encargada de Ventas')),
                ('PersonaPagos', models.CharField(blank=True, max_length=200, null=True, verbose_name='Persona Encargada de Pagos')),
                ('Propietario', models.CharField(blank=True, max_length=200, verbose_name='Propietario')),
                ('Direccion', models.CharField(blank=True, max_length=250, null=True, verbose_name='Dirección del Propietario')),
                ('TelefonoPropietario', models.PositiveBigIntegerField(verbose_name='Numero Telefonico del Propietario')),
                ('FaxPropietarion', models.CharField(blank=True, max_length=200, verbose_name='Fax del Propietario')),
                ('ReferenciaNombre', models.CharField(max_length=200, verbose_name='Nombre de la referencia Comercial')),
                ('ReferenciaContacto', models.CharField(max_length=200, verbose_name='Contacto de la referencia Comercial')),
                ('ReferenciaTelefono', models.CharField(max_length=200, verbose_name='Telefono de la referencia Comercial')),
                ('ReferenciaNombre2', models.CharField(blank=True, max_length=200, verbose_name='Nombre de la referencia Comercial')),
                ('ReferenciaContacto2', models.CharField(blank=True, max_length=200, verbose_name='Contacto de la referencia Comercial')),
                ('ReferenciaTelefono2', models.CharField(blank=True, max_length=200, verbose_name='Telefono de la referencia Comercial')),
                ('ReferenciaNombre3', models.CharField(blank=True, max_length=200, verbose_name='Nombre de la referencia Comercial')),
                ('ReferenciaContacto3', models.CharField(blank=True, max_length=200, verbose_name='Contacto de la referencia Comercial')),
                ('ReferenciaTelefono3', models.CharField(blank=True, max_length=200, verbose_name='Telefono de la referencia Comercial')),
                ('ReferenciaBancariaBanco', models.CharField(max_length=200, verbose_name='Banco de la referencia Bancaria')),
                ('ReferenciaBancariaCuenta', models.CharField(max_length=200, verbose_name='Cuenta de la referencia Bancaria')),
                ('ReferenciaBancariaTelefono', models.CharField(max_length=200, verbose_name='Telefono de la referencia Bancaria')),
                ('ReferenciaNombrePersonal', models.CharField(max_length=200, verbose_name='Nombre de la referencia Personal')),
                ('ReferenciaDireccionPersonal', models.CharField(max_length=200, verbose_name='Dirección de la referencia Personal')),
                ('ReferenciaTelefonoPersonal', models.CharField(max_length=200, verbose_name='Telefono de la referencia Personal')),
                ('ReferenciaNombrePersona2', models.CharField(blank=True, max_length=200, verbose_name='Nombre de la referencia Personal')),
                ('ReferenciaDireccionPersona2', models.CharField(blank=True, max_length=200, verbose_name='Dirección de la referencia Personal')),
                ('ReferenciaTelefonoPersona2', models.CharField(blank=True, max_length=200, verbose_name='Telefono de la referencia Personal')),
                ('ReferenciaNombrePersona3', models.CharField(blank=True, max_length=200, verbose_name='Nombre de la referencia Personal')),
                ('ReferenciaDireccionPersona3', models.CharField(blank=True, max_length=200, verbose_name='Dirección de la referencia Personal')),
                ('ReferenciaTelefonoPersona3', models.CharField(blank=True, max_length=200, verbose_name='Telefono de la referencia Personal')),
                ('DocumentosEntregados', models.CharField(blank=True, choices=[('RFC Empresa', 'RFC Empresa'), ('Identificación Oficial REP Legal', 'Identificación Oficial REP Legal'), ('Comp. Domicilio Empresa', 'Comp. Domicilio Empresa'), ('Comp. Domicilio REP Legal', 'Comp. Domicilio REP Legal'), ('Acta Constitutiva', 'Acta Constitutiva'), ('Pagaré con Aval', 'Pagaré con Aval'), ('Identificación Oficial Aval', 'Identificación Oficial Aval'), ('Comp. Domicilio Aval', 'Comp. Domicilio Aval'), ('Estados de Cuenta Recientes(3)', 'Estados de Cuenta Recientes(3)'), ('Estados Financieros Anual y Mensual', 'Estados Financieros Anual y Mensual')], max_length=200, verbose_name='Documentos Entregados')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UsuarioPromexCredito', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Solicitud de Credito',
                'ordering': ['-id'],
            },
        ),
    ]
