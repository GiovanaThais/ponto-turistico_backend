from rest_framework.serializers import ModelSerializer
from core.models import pontoTuristico

class pontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = pontoTuristico
        fields = ('id','nome','descricao','status','foto')