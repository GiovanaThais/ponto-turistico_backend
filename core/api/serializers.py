from rest_framework.serializers import ModelSerializer
from core.models import pontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
#from rest_framework.fields import SearializerMethodField
from atracoes.models import Atracao
from enderecos.models import Endereco

class pontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True) #relaçao muitos pra muitos
    endereco= EnderecoSerializer()
    class Meta:
        model = pontoTuristico
        fields = ('id','nome','descricao','status'
        ,'endereco','foto','atracoes','comentarios')
        read_only_fields = ['comentarios']

    def cria_atracoes(self, atracoes, ponto): 
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)
    
    def create(self, validated_data):
        atracoes = validated_data['atracoes'] 
        del validated_data['atracoes'] #manytomany relacionamentos

        #relacionamento com chave estrangeira FK
        endereco = validated_data['endereco']
        del validated_data['endereco']

        ponto = pontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.save()

        #relacionamento de 1-1
        
        return ponto