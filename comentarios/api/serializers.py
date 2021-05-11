from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario
#from comentarios.models import Avaliacao

class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('usuario','comentario','data','aprovado')
        #model = Avaliacao
        #fields = ('usuario','nota')