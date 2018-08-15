# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
#       return HttpResponse('Home page!')
        numeros =[1,2,3,4,5]
        nombre = 'Sistema Gestor de Corrección de Trabajos Prácticos'

        args = {'nombre': nombre}
        return render(request, 'accounts\login.html', args)
