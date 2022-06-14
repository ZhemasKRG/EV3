# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Carro(models.Model):
    cantidad = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    persona_id_persona = models.OneToOneField('Persona', models.DO_NOTHING, db_column='persona_id_persona')
    folio = models.AutoField(primary_key=True)
    producto_serie = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_serie')

    class Meta:
        managed = False
        db_table = 'carro'
        unique_together = (('persona_id_persona', 'folio'),)


class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=9)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'persona'


class PersonaUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    persona_id_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='persona_id_persona')
    tipo_usuario_id_tipo_usuario = models.ForeignKey('TipoUsuario', models.DO_NOTHING, db_column='tipo_usuario_id_tipo_usuario')
    password = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'persona_usuario'


class Producto(models.Model):
    serie = models.AutoField(primary_key=True)
    nombre_p = models.CharField(max_length=30, blank=True, null=True)
    precio = models.BigIntegerField(blank=True, null=True)
    foto = models.FileField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'producto'


class TipoUsuario(models.Model):
    id_tipo_usuario = models.BigIntegerField(primary_key=True)
    tipo_usuario = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'

