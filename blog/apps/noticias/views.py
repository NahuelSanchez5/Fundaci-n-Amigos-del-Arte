from django.shortcuts import render

def noticia_list(request):

    return render(request, 'ejemplo/post_list.html', {})
