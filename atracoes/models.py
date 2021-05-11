from django.db import models

class Atracao(models.Model):
    nome = models.CharField("nome", max_length=130)
    descricao= models.TextField(name='descricao')
    horario = models.CharField(name='horario', max_length=130)
    idade_min = models.IntegerField()
    foto = models.ImageField(upload_to= 'atracoes',null=True,blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table= 'atraçao'
        verbose_name = "Atraçao" 
        verbose_name_plural = "Atraçoes"
