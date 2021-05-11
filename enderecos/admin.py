from django.contrib import admin
from .models import Endereco

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['rua','bairro','cidade','estado','pais','complementos']
# Register your models here.
