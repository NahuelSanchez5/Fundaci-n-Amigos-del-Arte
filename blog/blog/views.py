from django.shortcuts import render

def Home(request):

	return render(request, 't_home.html')

def Nosotros(request):
    return render(request, 't_nosotros.html')
