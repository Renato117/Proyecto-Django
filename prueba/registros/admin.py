from django.contrib import admin
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno', 'created')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turno')
<<<<<<< HEAD
=======

>>>>>>> 70f741bcabd82be37e8a73db01994424bbbe7341
    list_per_page=2
    list_display_links=('matricula', 'nombre')
    list_editable=('turno',)

<<<<<<< HEAD
    def get_readonly_fields(self,request, obj=None):
        if request.user.groups.filter(name="Usuarios").exists():
            return ('created', 'updated', 'matricula', 'carrera', 'turno')
        else:
            return ('created', 'updated')
admin.site.register(Alumnos, AdministrarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')  # valores por defecto

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="GestorDeComentarios").exists():
            return ('created', 'id', 'alumno')
        return super().get_readonly_fields(request, obj)

admin.site.register(Comentario, AdministrarComentarios)


=======
    def get_readonly_fields(self, request, obj=None):
        #si el usuario pertenece al grupo de permisos "Usuario"
        if request.user.groups.filter(name="Usuarios").exists():
            #Bloquea los campos
            return ('created', 'updated', 'matricula', 'carrera', 'turno')
            #Cualquier otro usuario que no pertenece al grupo "Usuarios"
        else:
            #Bloquea los campos
            return ('created', 'updated')
                            
admin.site.register(Alumnos, AdministrarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment', 'created')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Administrador1").exists():
                return ('created', 'alumno',)
        else:
            #Bloquea los campos
            return ('created')
admin.site.register(Comentario, AdministrarComentarios)

>>>>>>> 70f741bcabd82be37e8a73db01994424bbbe7341
class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

<<<<<<< HEAD
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)
=======
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)
>>>>>>> 70f741bcabd82be37e8a73db01994424bbbe7341
