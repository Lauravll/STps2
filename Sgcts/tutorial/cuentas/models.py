# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from __future__ import unicode_literals

from django.db import models

class Usuarios(models.Model):
    usuario = models.CharField(primary_key=True, max_length=45)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    clave = models.CharField(max_length=25)
    tipo = models.CharField(max_length=25)

    def __unicode__(self):
        return self.usuario

class TrabajoPractico(models.Model):
    titulo = models.CharField(max_length=50)
    materia = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    idUsuario = models.ForeignKey('Usuarios', db_column='usuario')

    def __unicode__(self):
        return u'%s' % (self.titulo)

#Si quisieramos que el sistema tambien guarde informacion sobre las carreras y materias.
'''
class Materia(models.Model):
    nombre = models.CharField(max_length=40)
    carrera = models.ForeignKey("Carrera")

    def __unicode__(self):
        return u'%s' % (self.nombre)


class Carrera(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % (self.nombre)

class TrabajoPractico(models.Model):
    titulo = models.CharField(max_length=45)
    materia = models.ForeignKey("Materia")
    idUsuario = models.ForeignKey('Usuarios', db_column='usuario')

    def __unicode__(self):
        return u'%s' % (self.titulo)'''
