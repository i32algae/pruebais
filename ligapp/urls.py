from django.conf.urls import url, include, patterns
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
	url(r'^$', views.clasificacion, name='clasificacion'),
	url(r'^crearequipo/$', views.crearEquipo, name='crearEquipo'),
	url(r'^(?P<nomEquipo>\D+)/$', views.mostrarEquipo, name='mostrarEquipo'),
	url(r'^(?P<nombreEquipo>\D+)/modificar$', views.modEquipo, name='modEquipo'),
)+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
