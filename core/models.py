from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    #no Django precisa informar o que fazer caso o usuário seja deletado
    #Se o usuário dono desse evento for exluído da aplicação, exclui também todos os eventos dele

#pra exigir que a tabela chame evento
    class Meta:
        db_table = 'evento'

#sempre que alguem chamar esse objeto, ele automaticamente vai trazer o nome do título
    def __str__(self):
        return self.titulo