from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from atracoes.models import Atracao
from .serializers import AtracaoSerializer

class AtracoesViewSet(ModelViewSet):
    queryset= Atracao.objects.all()
    serializer_class = AtracaoSerializer

    #habilitando buscas na api usando djangoFilter
    filter_backends= (DjangoFilterBackend,)
    filter_fields = ('nome','descricao','horario')