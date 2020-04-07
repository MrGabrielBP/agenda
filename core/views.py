from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento

# Create your views here.
def consulta(request, titulo_evento):
    evento = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse('<h1>{} -- {}</h1>'.format(evento.titulo, evento.get_data_evento()))

#def index(request):
#    return redirect('/agenda/')

def lista_eventos(request):
    #evento = Evento.objects.get(id=1)
    #O objects é pra fazer uma consulta no id específico.

    evento = Evento.objects.all()
    #todos os objetos

    #usuario = request.user
    #evento = Evento.objects.filter(usuario=usuario)
    #É a mesma coisa do all só que agora eu estou fazendo um filtro.
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
