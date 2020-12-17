from rest_framework import generics
from rest_framework.generics import get_object_or_404


from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

from rest_framework import permissions


from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from .permissions import IsSuperUser


""" 
API V1
"""
# Lista e cria Cursos (GET e POST)
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


# Obtem um curso específico pelo id, atualiza e deleta (GET, PUT, DELETE)
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


# Lista e cria Avaliações (GET e POST)
class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()


# Obtem uma avaliação específica pelo id, atualiza e deleta (GET, PUT, DELETE)
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                                     curso_id=self.kwargs.get('curso_pk'),
                                     pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


""" 
API V2
"""

class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsSuperUser,
        permissions.DjangoModelPermissions,
    )

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):

        # Define a paginação dos dados que serão apresentados
        self.pagination_class.page_size = 2
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


# class AvaliacaoViewSet(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     viewsets.GenericViewSet
#     ):

#     queryset = Avaliacao.objects.all()
#     serializer_class = AvaliacaoSerializer


