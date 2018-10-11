# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, HttpResponseServerError
from clases.dbpython import *
from clases.Usuario import Usuario, Sesion
from clases.Peticion import Peticion
from clases.Admin import Admin
from clases.Actividad import Actividad
#Imports necesarios si queremos usar la bd de Django
from .models import Usuarios
from django.shortcuts import get_object_or_404, render

# Create your views here.
def login(request):
#   return HttpResponse('Home page!')
	numeros = [1,2,3,4,5]
	titulo = 'Sistema Gestor de Corrección de Trabajos Prácticos'
	args = {'nombre1': titulo, 'numeros1': numeros}
	return render(request, 'cuentas\login.html', args)

def proyecto(request, usuario):
	nombreP = 'Sistema Gestor de Corrección de Trabajos Prácticos'
	sesion=Sesion()#creo la instancia de la clase Sesion para pder realizar acciones sobre el usuario
	usuario2=sesion.traerUsuarioComprobado(usuario)
	args = {'usuario1': usuario2, 'nombreP': nombreP}
	return render(request, 'cuentas/proyecto.html', args)

#Version sin utilizar la base de datos de django
"""
def inicio(request):
	numeros5 =[1,2,3,4,5]
	nombre5 = 'Sistema Gestor de Corrección de Trabajos Prácticos'
	#args = {'nombre1': nombre5, 'numeros1': numeros5}
	nombre = request.POST.get('usuariol')
	print(nombre)
	clave = request.POST.get('clavel')
	print(clave)
	user =Usuario(None,None,None,None,None)#creo un user vacio para luego cargarlo y llamarlo desde otra clase
	sesion=Sesion()#creo la instancia de la clase Sesion para pder realizar acciones sobre el usuario
	try:
		usuario=sesion.traerUsuarioSes(nombre,clave)
		rol =usuario.getTipo()#guardo el tipo de usuario en rol para luego decidir a que pantalla es dirigido
		print(rol)
		if(rol=="Docente"):
			args = {'nombre1': nombre5, 'numeros1': numeros5, 'usuario1': usuario}
			return render(request, 'cuentas/inicio.html', args)
		else:
			if(rol=="Administrador"):
				return render(request, 'cuentas/inicio.html', args)
	except Exception:
		print("Error de logueo")
		return render(request, 'cuentas/elogin.html', args)

"""

#Utilizando la base de django
def inicio(request):
	numeros5 =[1,2,3,4,5]
	nombreP = 'Sistema Gestor de Corrección de Trabajos Prácticos'
	nombre = request.POST.get('usuariol')
	print(nombre)
	clave = request.POST.get('clavel')
	print(clave)
	try:
		#usuario = get_object_or_404(Usuarios, pk=nombre)
		usuario = Usuarios.objects.get(pk=nombre)
		rol = usuario.tipo #guardo el tipo de usuario en rol para luego decidir a que pantalla es dirigido
		print(rol)
		print(usuario)
		if(rol=="Docente"):
			args = {'nombreP': nombreP, 'numeros1': numeros5, 'usuario1': usuario}
			return render(request, 'cuentas/inicio.html', args)
		else:
			if(rol=="Administrador"):
				return render(request, 'cuentas/inicio.html', args)
	except Exception:
		print("Error de logueo")
		return render(request, 'cuentas/elogin.html', args)


def crear(request, usuario):
	nombreP = 'Sistema Gestor de Corrección de Trabajos Prácticos'
	nombre = request.POST.get('nombret')
	print(nombre)
	materia = request.POST.get('materia')
	print(materia)
	carrera = request.POST.get('carrera')
	print(carrera)
	user =Usuario(None,None,None,None,None)#creo un user vacio para luego cargarlo y llamarlo desde otra clase
	sesion=Sesion()#creo la instancia de la clase Sesion para pder realizar acciones sobre el usuario
	usuario2=sesion.traerUsuarioComprobado(usuario)
	# Intentar conectar a la base de datos
	try:
		print("Usuario: "+ usuario2.getNombre())
		#con la instancia user accedo al metodo agregarTp de Usuario() y le paso por parametro las entradas del teclado
		numero = usuario2.crearTrabajoPractico(nombre, materia, carrera)
		print("TP " + numero +" creado con éxito")
	except Exception:
		print("Error al insertar TP")
	args = {'nombreP': nombreP, 'idtrabajo': numero, 'nombre': nombre, 'materia': materia, 'carrera': carrera, 'usuario1': usuario}
	#Deberia estar en trabajo y no en actividad
	return render(request, 'cuentas/htrabajos.html', args)

def finalizar(request, usuario, idtrabajo):
	titulo = 'Sistema Gestor de Corrección de Trabajos Prácticos'
	args = {'nombre1': titulo}
	cantidad = request.POST.get('cantidad')
	i = 1
	cp = int(cantidad)
	print(cp)
	#Obtengo la cantidad de preguntas que eligió el usuario, por ahora esta armado en base a 3 respuestas
	while i<= cp:
		#Concateno la información con el id de la pregunta
		respuesta1 = "input{}-1".format(i)
		respuesta2 = "input{}-2".format(i)
		respuesta3 = "input{}-3".format(i)
		consigna = "consigna{}".format(i)
		#Obtengo la información contenida en los imput, solo trabajo con 3 por el momento
		r1 = request.POST.get(respuesta1)
		r2 = request.POST.get(respuesta2)
		r3 = request.POST.get(respuesta3)
		c = request.POST.get(consigna)
		actividad = Actividad(idtrabajo, i, c, r1, r2, r3, 1)
		actividad.crearActividad(idtrabajo)
		i += 1
	return render(request, 'cuentas/htrabajos.html', args)

#Lo agregué solamente para hacer un par de test
if __name__ == '__main__':
	guardar()
	home()
