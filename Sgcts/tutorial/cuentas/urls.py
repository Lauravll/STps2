from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
import cuentas.views
urlpatterns = [

# para referenciar views.py
    url(r'^$', views.login),
	
#Como no tenemos acceso debemos importarla. En realidad estas url ya estan mapeadas en el archivo de urls principal, pero quise probar con ambos ejemplos.
    url(r'^proyecto/$', login, {'template_name': 'cuentas/proyecto.html'}),
    url(r'^crear/$', login, {'template_name': 'cuentas/htrabajos.html'}),
	url(r'^inicio/$', login, {'template_name': 'cuentas/inicio.html'}),

#Para acceder http://127.0.0.1:8000/cuentas/inicio/

]
