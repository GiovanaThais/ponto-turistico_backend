from django.contrib import admin
from .models import Comentario
#from .models import Avaliacao

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario','comentario','aprovado','notas']

#@admin.register(Avaliacao)
#class AvaliacaoAdmin(admin.ModelAdmin):
    #list_display = ['usuario','nota']
# Register your models here.
