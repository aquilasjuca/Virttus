from django.shortcuts import render


def inicio(request):
    return render(request, 'virttus_app/inicio.html')


def contatos(request):
    return render(request, 'virttus_app/contatos.html')


def profissionais(request):
    return render(request, 'virttus_app/profissionais.html')


def servicos(request):
    return render(request, 'virttus_app/servicos.html')


def localizacao(request):
    return render(request, 'virttus_app/localizacao.html')
