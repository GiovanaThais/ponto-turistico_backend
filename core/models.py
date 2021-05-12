from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
#from comentarios.models import Avaliacao
from enderecos.models import Endereco


class pontoTuristico(models.Model):
    nome = models.CharField('nome', max_length=130)
    descricao= models.TextField(name='descricao')
    status= models.BooleanField(name='status',default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    #avaliacao = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE,null=True,blank=True)
    foto = models.ImageField(upload_to= 'pontos_turisticos',null=True,blank=True)

    def __str__(self):
        return self.nome
    

    class Meta:
        db_table= 'ponto turistico'
        verbose_name= "Ponto turistico"
        verbose_name_plural= "Pontos turisticos"


