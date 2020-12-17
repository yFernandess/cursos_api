from rest_framework import serializers
from django.db.models import Avg

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:

        # Criado configuração para não apresentar o campo email, será somente escrita (cadastro)
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao

        # Campos que serão apresentados
        fields = (
            'id',
            'curso',
            'name',
            'email',
            'comment',
            'avaliacao',
            'creation',
            'active'
        )
    
    def validate_avaliacao(self, value):
        if value in range(1, 6): # 1, 2, 3, 4, 5
            return value
        raise serializers.ValidationError('A avaliação precisa ser um inteiro entre 1 e 5')


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    """
    Hyper linked Related Field - É interessante utilizar dessa abordagem
    caso exista um cenário de muitas avaliações e no retorno dos dados
    é disponibilizado um link das avaliações do curso
    """
    avaliacoes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='avaliacao-detail'
    )

    """
    Primary Key Related Field - Caso houver uma grande quantidade de avaliações
    então é recomendado o uso de PrimaryKeyRelatedField. Diferente do Hyper linked
    related field, ele apenas devolve o id da avaliação. A consulta da mesma deve ser
    feita pelo endpoint de avaliações se necessário
    """

    # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'title',
            'url',
            'creation',
            'active',
            'avaliacoes',
            'media_avaliacoes'
        )

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2) / 2