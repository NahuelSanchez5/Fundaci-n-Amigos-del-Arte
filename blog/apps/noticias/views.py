from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Noticia, Categoria, Comentario
from django.urls import reverse_lazy

@login_required
def Listar_Noticias(request):
    contexto = {}

    id_categoria = request.GET.get('id', None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia = id_categoria)
    else:
        n = Noticia.objects.all()

    contexto['noticias'] = n

    cat = Categoria.objects.all().order_by('nombre')
    contexto['categorias'] = cat
    
    return render(request, 'noticias/listar.html', contexto)

@login_required    
def Detalle_Noticias(request,pk):
    contexto = {}
    n = Noticia.objects.get(pk = pk) #RETORNA SOLO UN OBJETO
    contexto['noticia'] = n

    c = Comentario.objects.filter(noticia= n)

    contexto['comentarios'] = c
    

    return render(request, "noticias/detalle.html", contexto)

@login_required
def Comentar_Noticia(request):
    com = request.POST.get('comentario', None)
    usu = request.user
    noti = request.POST.get('id_noticia', None)#obtengo la pk
    noticia = Noticia.objects.get(pk=noti)#busco la noticia con esa pk
    coment = Comentario.objects.create(usuario=usu, noticia= noticia, texto=com)

    return redirect(reverse_lazy('noticias:detalle', kwargs={'pk':noti}))


