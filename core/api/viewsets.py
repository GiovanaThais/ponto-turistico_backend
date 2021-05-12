from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.filters import SearchFilter
from rest_framework.permissions import DjangoModelPermissions # IsAuthenticatedOrReadOnly # IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication 
from core.models import pontoTuristico
from .serializers import pontoTuristicoSerializer
from django.http import HttpResponse

class pontoTuristicoViewSet(viewsets.ModelViewSet):
    
    serializer_class = pontoTuristicoSerializer  #incluir campos no json
    filter_backends = [filters.SearchFilter] #para campos de pesquisa (searchFielter)
    search_fields = ['nome', 'descricao'] #filtro de pesquisa
    #lookup_field = 'nome' localizar registro atraves do nome e n do id
    permission_classes = [DjangoModelPermissions] #permite setar permissão para cada endpoint
    authentication_classes = [TokenAuthentication]
    
    def get_queryset(self):
        id = self.request.query_params.get('id', None) #filtrar por ID (opcional[none])
        nome = self.request.query_params.get('nome', None) #filtrar por nome
        descricao = self.request.query_params.get('descricao', None) #filtrar por descricao
        queryset= pontoTuristico.objects.all()

    #filtrando por query string
        if id is not None:
            queryset = queryset.filter(id__iexact=id)

        if nome is not None:
            queryset = queryset.filter(nome__iexact=nome)
        
        if descricao is not None:
            queryset = queryset.filter(descricao__iexact=descricao)
        
        return queryset
        #return pontoTuristico.objects.filter(status= True)

    def list(self,request,*args, **kwargs):
        return super(pontoTuristico, self).list(request, *args, **kwargs)
#sobrescrevendo action de get , post e delete
    
    def create(self, request, *args, **kwargs):
        return super(pontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(pontoTuristicoViewSet, self).destroy(request, *args, **kwargs)
        
    def retrieve(self, request, *args, **kwargs):
        return super(pontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)
        
    def update(self, request, *args, **kwargs):
        return super(pontoTuristicoViewSet, self).update(request, *args, **kwargs)
        
    def partial_update(self, request, *args, **kwargs):
        return super(pontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['post'], detail=True) #usar datail = true para pegar o pk 
    def denunciar(self, request, pk=None):
        pass
        # return super(PontoTuristicoViewSet, self).teste(request, *args, **kwargs)
    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, id):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(id=id)

        ponto.atracoes.set(atracoes)

        ponto.save()
        return HttpResponse('Ok')