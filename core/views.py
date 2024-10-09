from rest_framework import generics
from .models import Livro
from .serializers import LivroSerializer
from django_filters import rest_framework as filters

class LivroFilter(filters.FilterSet):
    class Meta:
        model = Livro
        fields = {
            'titulo': ['exact', 'icontains'],
            'autor': ['exact', 'icontains'],
            'categoria': ['exact', 'icontains'],
        }

class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']
    search_fields = ['titulo', 'autor', 'categoria']

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
