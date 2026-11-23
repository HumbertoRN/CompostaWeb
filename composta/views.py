from django.shortcuts import render


def home(request):
    return render(request, 'composta/home.html')


def como_hacer(request):
    return render(request, 'composta/como_hacer.html')



def materiales(request):
    return render(request, 'composta/materiales.html')



def beneficios(request):
    return render(request, 'composta/beneficios.html')



def preguntas(request):
    return render(request, 'composta/preguntas.html')



def creditos(request):
    return render(request, 'composta/creditos.html')
