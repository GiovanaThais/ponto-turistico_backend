from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
#from comentarios.models import Avaliacao
from .serializers import ComentarioSerializer

class ComentarioViewSet(ModelViewSet):
    queryset= Comentario.objects.filter(aprovado=True)
    #queryset = Avaliacao.objects.all()
    serializer_class = ComentarioSerializer
    