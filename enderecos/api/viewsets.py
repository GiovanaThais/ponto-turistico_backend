from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from .serializers import EnderecoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class EnderecoViewSet(ModelViewSet):
    queryset= Endereco.objects.all()
    serializer_class = EnderecoSerializer

    #habilitando buscas na api usando djangoFilter
    filter_backends= (DjangoFilterBackend,)
    filter_fields = ('rua','cidade','estado')