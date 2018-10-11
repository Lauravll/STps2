from django.conf.urls import url, include
import cuentas.views
from django.contrib.auth.views import login, logout_then_login
from django.contrib import admin

urlpatterns = [
	#1) Podemos mapear la aplicacion creada, en este caso cuentas (Dentro de cuentas debemos crear su propio archivo urls.py -> cuentas\urls.py)
    url(r'^cuentas/', include('cuentas.urls')),
	
	#2) Podemos mapear todas las url directamente 
    url(r'^inicio/', cuentas.views.inicio),
    url(r'^$', cuentas.views.login),
	url(r'^logout.html', logout_then_login),
	url(r'^proyecto/(?P<usuario>.+)$', cuentas.views.proyecto),
	url(r'^crear/(?P<usuario>.+)$', cuentas.views.crear),
    url(r'^finalizar/(?P<usuario>.+)/(?P<idtrabajo>.+)$', cuentas.views.finalizar),
	
	# Uncomment the next line to enable the admin:
	#Administrador de Django, para nuestro proyecto no sirve de mucho.
    url(r'^admin/', include(admin.site.urls)),
]
