<<<<<<< HEAD
from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404
import datetime
=======
import datetime
from django.shortcuts import render
from .models import Alumnos, Comentario
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404
>>>>>>> 70f741bcabd82be37e8a73db01994424bbbe7341
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages

<<<<<<< HEAD

=======
>>>>>>> 70f741bcabd82be37e8a73db01994424bbbe7341
# Create your views here.

def registros(request):
    alumnos=Alumnos.objects.all()
#all recupera todos los objetos del modelo (registros de la tabla alumnos)

    return render(request,"registros/principal.html",{'alumnos':alumnos})
#Indicamos el lugar donde se renderizara el resultado de esta vista
# y enviamos la lista de alumnos recuperados

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            comentarios=ComentarioContacto.objects.all()
            return render(request,'registros/comentarioContacto.html', {'comentarios':comentarios})
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request, 'registros/contacto.html',{'form': form})

def contacto(request):
    return render(request,"registros/contacto.html")
#Indicamos el lugar donde se renderizará el resultado de esta vista

def comentarioContacto(request):
    comentarios=ComentarioContacto.objects.all()
    return render(request,'registros/comentarioContacto.html', {'comentarios':comentarios})

def eliminarComentarioContacto( request, id,
        confirmacion='registros/confirmarEliminacion.html'):
        comentario = get_object_or_404(ComentarioContacto, id=id)
        if request.method=='POST':
            comentario.delete()
            comentarios=ComentarioContacto.objects.all()
            return render(request,"registros/comentarioContacto.html", {'comentarios':comentarios})
        return render(request, confirmacion, {'object':comentario})

def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    #get permite establecer una condicionante a la consulta y recupera el objetos
    #del modelo que cumple la condición ( registro de la tabla ComentariosContacto.)
    #get se emplea cuando se sabe que solo hay un objeto que coincide con su
    #consulta

    return render(request,"registros/formEditarComentario.html",{'comentario':comentario})
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de alumnos recuperacos

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    #Referenciamos que el elemento del formulario pertenece al comentario
    # ya existente
    if form.is_valid():
        form.save() #si el registro ya existe, se modifica.
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/comentarioContacto.html",{'comentarios':comentarios})
    #Si el formulario no es valido nos regresa al formulario para verificar
    #datos
    return render(request,"registros/formEditarComentario.html",{'comentario':comentario})

def consultar1(request):
<<<<<<< HEAD
=======
    #con una sola condición
>>>>>>> 70f741bcabd82be37e8a73db01994424bbbe7341
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar3(request):
<<<<<<< HEAD
    alumnos=Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "imagen")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
=======
    #Si solo deseamos recuperar ciertos datos agregamos la #función only,
    #listando los campos que queremos obtener de #la función emplear
    # filter() o #en el ejemplo all() 
    alumnos=Alumnos.objects.only("matricula", "nombre", "carrera", "turno", "imagen")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno_contains="Vesp") #_contains: LIKE
>>>>>>> 70f741bcabd82be37e8a73db01994424bbbe7341
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
<<<<<<< HEAD
    return render(request, "registros/consultas.html",{'alumnos':alumnos})


def consultar6(request):
    fechaInicio = datetime.date(2022,7,1)
    fechaFin = datetime.date(2022,7,13)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request, "registros/consultas.html", {'alumnos':alumnos})

def consultar7 (request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains='No inscrito')
    return render (request, "registros/consultas.html", {'alumnos':alumnos})

def comentarios_fecha(request):
    comentarios = ComentarioContacto.objects.filter(created__range=['2025-07-08', '2025-07-09'])
    return render(request, 'registros/comentarioContacto.html', {'comentarios': comentarios})

def comentarios_con_palabra(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__icontains='primero')
    return render(request, 'registros/comentarioContacto.html', {'comentarios': comentarios})

def comentarios_de_usuario(request):
    comentarios = ComentarioContacto.objects.filter(usuario='renato')
    return render(request, 'registros/comentarioContacto.html', {'comentarios': comentarios})

def solo_mensajes(request):
    comentarios = ComentarioContacto.objects.only('mensaje') 
    return render(request, 'registros/comentarioContacto.html', {'comentarios': comentarios})

def comentarios_sin_palabra(request):
    comentarios = ComentarioContacto.objects.exclude(mensaje__icontains='inscrito')
    return render(request, 'registros/comentarioContacto.html', {'comentarios': comentarios})
=======
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2022, 7, 1)
    fechaFin = datetime.date(2022, 7, 13)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
    #Consultando entre modelos
    alumnos=Alumnos.objects.filter(comentario__coment__contains='No inscrito')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})


def consultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos Where carrera="TI" ORDER BY turno DESC')

    return render(request,"registros/consultas.html", {'alumnos':alumnos})


def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request,"registros/seguridad.html", {'nombre':nombre})

def consultarNueva1(request):
    fechaInicio = datetime.date(2025, 7, 8)
    fechaFin = datetime.date(2025, 7, 9)
    comentarios =ComentarioContacto.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,'registros/comentariosContactos.html', {'comentarios':comentarios})

def consultarNueva2(request):
    comentarios=ComentarioContacto.objects.only("mensaje")
    return render(request,'registros/comentariosContactos.html', {'comentarios':comentarios})

def consultarNueva3(request):
    comentarios=comentarioContacto.objects.filter(mensaje__contains='Buenas tardes')
    return render(request,'registros/comentariosContactos.html', {'comentarios':comentarios})

def consultarNueva4(request):
    comentarios=comentarioContacto.objects.filter(usuario__in=["Elena", "Juan"])
    return render(request,"registros/comentariosContactos.html",{'comentarios':comentarios})

def consultarNueva5(request):
    comentarios=comentarioContacto.objects.filter(mensaje__istartswith=["Hola"])
    return render(request,"registros/comentariosContactos.html",{'comentarios':comentarios})

>>>>>>> 70f741bcabd82be37e8a73db01994424bbbe7341

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
<<<<<<< HEAD
        return render(request, "registros/archivos.html", {'archivo': Archivos})
    
def consultasSQL(request):
    alumnos = Alumnos.objects.raw(
        'SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC'
    )
    return render(request, "registros/consultas.html", {'alumnos': alumnos})
    
def seguridad(request, nombre=None):
        nombre = request.GET.get('nombre')
        return render(request, "registros/seguridad.html", {'nombre':nombre})
=======
        return render(request,"registros/archivos.html",{'archivos':Archivos})
>>>>>>> 70f741bcabd82be37e8a73db01994424bbbe7341
