from django.shortcuts import render, HttpResponse

menu="""
<a href="/">Home</a>
<a href="/formulario">Registrar</a>
<a href="/contacto">Contactanos</a>
<a href="/ejemplo">Ejemplo</a>

"""

# Create your views here.
def principal(request):
        return render(request, "inicio/principal.html")

def formulario(request):
        return render(request, "inicio/formulario.html")

def contacto(request):
        return render(request, "inicio/contacto.html")

def ejemplo(request):
        return render(request, "inicio/ejemplo.html")

