from django.db import models

class Endereco(models.Model):
    rua = models.CharField("rua", max_length=150)
    bairro = models.CharField("bairro", max_length=100)
    cidade = models.CharField("cidade", max_length=120)
    estado = models.CharField("estado", max_length=150)
    pais = models.CharField("país", max_length=70)
    complementos = models.CharField("complementos", max_length=100, null=True,blank=True)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)
    #nome_ponto_turistico = models.ForeignKey(PontoTuristico,on_delete=models.CASCADE, related_name='endereco_ponto',verbose_name='ponto turistico')

    def __str__(self):
        return self.rua
# Create your models here.
