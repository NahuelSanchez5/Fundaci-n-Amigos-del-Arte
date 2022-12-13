from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Noticia

@login_required
def Listar_Noticias(request):
    contexto = {}

    n = Noticia.objects.all()

    contexto['noticias'] = n
    
    return render(request, 'noticias/listar.html', contexto)

@login_required    
def Detalle_Noticias(request,pk):
    contexto = {}
    n = Noticia.objects.get(pk = pk) #RETORNA SOLO UN OBJETO
    contexto['noticia'] = n

    return render(request, "noticias/detalle.html", contexto)


