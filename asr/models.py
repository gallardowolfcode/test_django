# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aseguradora(models.Model):
    nombre_aseguradora = models.CharField(max_length=80)
    activo_aseguradora = models.IntegerField()

   


class Cliente(models.Model):
    id_persona = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=250, blank=True, null=True)
    rfc = models.CharField(max_length=25, blank=True, null=True)
    curp = models.CharField(max_length=18, blank=True, null=True)
    numero_cliente = models.CharField(max_length=20, blank=True, null=True)
    referencia_cliente = models.CharField(max_length=850, blank=True, null=True)
    activo_enviar_email_cliente = models.IntegerField(blank=True, null=True)
    activo_enviar_whats_cliente = models.IntegerField(blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    latitud_cliente = models.CharField(max_length=25, blank=True, null=True)
    longitud_cliente = models.CharField(max_length=25, blank=True, null=True)
    id_estado_civil = models.IntegerField(blank=True, null=True)
    observaciones_cliente = models.CharField(max_length=850, blank=True, null=True)

    


class ClienteFamilia(models.Model):
    nombre_familia = models.CharField(max_length=150, blank=True, null=True)
    parentezco_familia = models.CharField(max_length=80, blank=True, null=True)
    fecha_nacimiento_familia = models.DateField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)

    


class Estado(models.Model):
    nombre_estado = models.CharField(max_length=50)
    activo_estado = models.IntegerField()



class EstadoCivil(models.Model):
    nombre_estado_civil = models.CharField(max_length=80, blank=True, null=True)
    activo_estado_civil = models.IntegerField(blank=True, null=True)

    


class Estatu(models.Model):
    nombre_estatu = models.CharField(max_length=80)
    activo_estatu = models.IntegerField()

    


class FormaPago(models.Model):
    nombre_forma_pago = models.CharField(max_length=50, blank=True, null=True)
    activo_forma_pago = models.IntegerField(blank=True, null=True)

   


class MetodoPago(models.Model):
    nombre_metodo_pago = models.CharField(max_length=80, blank=True, null=True)
    activo_metodo_pago = models.IntegerField(blank=True, null=True)

    


class Moneda(models.Model):
    nombre_moneda = models.CharField(max_length=80)
    activo_moneda = models.IntegerField()

    


class Perfil(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    no_cliente = models.IntegerField(blank=True, null=True)
    idusers = models.IntegerField(blank=True, null=True)

    


class Persona(models.Model):
    nombre_persona = models.CharField(max_length=350)
    apellido_persona = models.CharField(max_length=350)
    fecha_nacimiento_persona = models.DateField()
    telefono_persona = models.CharField(max_length=30)
    telefono_casa_persona = models.CharField(max_length=25, blank=True, null=True)
    telefono_oficina_persona = models.CharField(max_length=25, blank=True, null=True)
    calle_persona = models.CharField(max_length=100, blank=True, null=True)
    cruzamiento_persona = models.CharField(max_length=100, blank=True, null=True)
    numero_interior_persona = models.CharField(max_length=10, blank=True, null=True)
    codigo_postal_persona = models.CharField(max_length=7, blank=True, null=True)
    localidad_persona = models.CharField(max_length=150, blank=True, null=True)
    municipio_persona = models.CharField(max_length=150, blank=True, null=True)

    


class Poliza(models.Model):
    numero_poliza = models.CharField(max_length=20, blank=True, null=True)
    id_vendedor = models.IntegerField(blank=True, null=True)
    id_producto = models.IntegerField(blank=True, null=True)
    periodo_inicio_poliza = models.DateTimeField(blank=True, null=True)
    periodo_fin_poliza = models.DateTimeField(blank=True, null=True)
    id_aseguradora = models.IntegerField(blank=True, null=True)
    prima_poliza = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    archivo_poliza = models.CharField(max_length=500, blank=True, null=True)
    periodo_gracia_poliza = models.CharField(max_length=250, blank=True, null=True)
    id_forma_pago = models.IntegerField(blank=True, null=True)
    periodo_redencion_poliza = models.CharField(max_length=250, blank=True, null=True)
    id_metodo_pago = models.IntegerField(blank=True, null=True)
    id_estatu = models.IntegerField(blank=True, null=True)
    suma_asegurada_poliza = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)

    


class PolizaBien(models.Model):
    id_poliza = models.IntegerField(blank=True, null=True)
    nombre_poliza_bien = models.IntegerField(blank=True, null=True)
    activo_poliza_bien = models.IntegerField(blank=True, null=True)

    


class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50, blank=True, null=True)
    descripcion_producto = models.CharField(max_length=350, blank=True, null=True)
    activo_producto = models.IntegerField(blank=True, null=True)
    id_moneda = models.IntegerField(blank=True, null=True)
    id_producto_tipo = models.IntegerField(blank=True, null=True)
    id_producto_categoria = models.IntegerField(blank=True, null=True)
    clave_producto = models.CharField(max_length=10, blank=True, null=True)

    


class ProductoCategoria(models.Model):
    nombre_producto_categoria = models.CharField(max_length=100, blank=True, null=True)
    activo_producto_categoria = models.IntegerField(blank=True, null=True)

    


class ProductoTipo(models.Model):
    nombre_producto_tipo = models.CharField(max_length=80, blank=True, null=True)
    activo_producto_tipo = models.IntegerField(blank=True, null=True)

    


# class Rol(models.Model):
#     idrol = models.AutoField(primary_key=True)
#     descripcion = models.CharField(max_length=60, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'rol'


# class Users(models.Model):
#     idusers = models.AutoField(primary_key=True)
#     user = models.CharField(max_length=50, blank=True, null=True)
#     password = models.CharField(max_length=50, blank=True, null=True)
#     fecha_registro = models.DateTimeField(blank=True, null=True)
#     estatus = models.IntegerField(blank=True, null=True)
#     idrol = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'users'


class Vendedor(models.Model):
    id_persona = models.IntegerField()
    numero_vendedor = models.CharField(max_length=20)
    comision_vendedor = models.FloatField()
    observacion_vendedor = models.CharField(max_length=350)
