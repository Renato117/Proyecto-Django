"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from registros import views as viewsRegistro
from django.conf import settings
<<<<<<< HEAD

=======
>>>>>>> 70f741bcabd82be37e8a73db01994424bbbe7341

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.principal, name="Principal"),
    path('', viewsRegistro.registros, name="Principal"),
    path('contacto/',viewsRegistro.contacto,name="Contacto"),
    #path('contacto/',views.contacto, name="Contacto"),
    path('formulario/',views.formulario,name="Formulario"),
    path('registar/',viewsRegistro.registrar,name="Registrar"),
    path('comentarios/',viewsRegistro.comentarioContacto, name="Comentarios"),
    path('eliminarComentario/<int:id>/',viewsRegistro.eliminarComentarioContacto,name='Eliminar'),
    path('formEditarComentario/<int:id>/',viewsRegistro.consultarComentarioIndividual, name='ConsultaIndividual'),
    path('editarComentario/<int:id>/',viewsRegistro.editarComentarioContacto,name='Editar'),
<<<<<<< HEAD
    path('consultas1',viewsRegistro.consultar1,name='Consultas'),
    path('consultas2',viewsRegistro.consultar2,name='Consultas2'),
    path('consultas3',viewsRegistro.consultar3,name='Consultas3'),
    path('consultas4',viewsRegistro.consultar4,name='Consultas4'),
    path('consultas5',viewsRegistro.consultar5,name='Consultas5'),
    path('consultas6',viewsRegistro.consultar6,name='Consultas6'),
    path('consultas7',viewsRegistro.consultar7,name='Consultas7'),
    path('comentarios_fecha/', viewsRegistro.comentarios_fecha, name='ComentariosFecha'),
    path('comentarios_con_palabra/', viewsRegistro.comentarios_con_palabra, name='ComentariosConPalabra'),
    path('comentarios_de_usuario/', viewsRegistro.comentarios_de_usuario, name='ComentariosDeUsuario'),
    path('solo_mensajes/', viewsRegistro.solo_mensajes, name='SoloMensajes'),
    path('comentarios_sin_palabra/', viewsRegistro.comentarios_sin_palabra, name='ComentariosSinPalabra'),
    path('subir',viewsRegistro.archivos, name="Subir"),
    path('consultasSQL', viewsRegistro.consultasSQL, name="Sql"),
    path('seguridad', viewsRegistro.seguridad, name="Seguridad"),

=======
    path('consultas1', viewsRegistro.consultar1, name="Consultas"),
    path('consultas2', viewsRegistro.consultar2, name="Consultas"),
    path('consultas3', viewsRegistro.consultar3, name="Consultas"),
    path('consultas4', viewsRegistro.consultar4, name="Consultas"),
    path('consultas5', viewsRegistro.consultar5, name="Consultas"),
    path('consultas6', viewsRegistro.consultar6, name="Consultas"),
    path('consultas7', viewsRegistro.consultar7, name="Consultas"),
    path('consultasNueva1', viewsRegistro.consultarNueva1, name="Consultas"),
    path('consultasNueva2', viewsRegistro.consultarNueva2, name="Consultas"),
    path('consultasNueva3', viewsRegistro.consultarNueva3, name="Consultas"),
    path('consultasNueva4', viewsRegistro.consultarNueva4, name="Consultas"),
    path('consultasNueva5', viewsRegistro.consultarNueva5, name="Consultas"),
    path('consultasSQL', viewsRegistro.consultasSQL, name="Sql"),
    path('seguridad', viewsRegistro.seguridad, name="Seguridad"),
    path('subir',viewsRegistro.archivos,name="Subir"),
    
    
>>>>>>> 70f741bcabd82be37e8a73db01994424bbbe7341
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)