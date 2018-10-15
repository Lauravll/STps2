# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Actividades(models.Model):
    idtrabajo = models.ForeignKey('Trabajos', models.DO_NOTHING, db_column='idTrabajo')  # Field name made lowercase.
    numero = models.IntegerField()
    consigna = models.CharField(max_length=250)
    respuesta1 = models.CharField(max_length=250)
    respuesta2 = models.CharField(max_length=250)
    respuesta3 = models.CharField(max_length=250)
    correcta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'actividades'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Peticiones(models.Model):
    idpeticion = models.AutoField(db_column='idPeticion', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    clave = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'peticiones'


class Trabajos(models.Model):
    idtrabajo = models.AutoField(db_column='idTrabajo', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=45)
    materia = models.CharField(max_length=45)
    carrera = models.CharField(max_length=45)
    usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='usuario')

    class Meta:
        managed = False
        db_table = 'trabajos'


class Usuarios(models.Model):
    usuario = models.CharField(primary_key=True, max_length=45)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    clave = models.CharField(max_length=25)
    tipo = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'usuarios'


class Usuariosxpeticiones(models.Model):
    usuario = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='usuario', primary_key=True)
    idpeticion = models.ForeignKey(Peticiones, models.DO_NOTHING, db_column='idPeticion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuariosxpeticiones'
        unique_together = (('usuario', 'idpeticion'),)
