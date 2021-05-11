from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField("comentários")
    data = models.DateField("data", auto_now_add=True)
    aprovado = models.BooleanField("status", default=True)
    notas = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.usuario.username

    class Meta:
        db_table= 'comentario'
        verbose_name= "Comentario"
        verbose_name_plural= "Comentarios"

'''class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avaliacao_comentario',verbose_name='Usuario')
    nota = models.DecimalField(max_digits=3, decimal_places=2)
    data = models.DateField("nota", auto_now_add=True)

    def __str__(self):
        return self.usuario.username

    class Meta:
        db_table= 'avaliacao'
        verbose_name= "Avaliaçao"
        verbose_name_plural= "Avaliaçoes"
# Create your models here.''' 
