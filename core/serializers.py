from rest_framework import serializers
from .models import Livro, Autor, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'  # Inclui todos os campos do modelo

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'  # Inclui todos os campos do modelo

class LivroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer()  # Incluindo o serializer de Autor
    categoria = CategoriaSerializer()  # Incluindo o serializer de Categoria

    class Meta:
        model = Livro
        fields = '__all__'  # Inclui todos os campos do modelo

    def create(self, validated_data):
        # Cria instâncias de Autor e Categoria se necessário
        autor_data = validated_data.pop('autor')
        categoria_data = validated_data.pop('categoria')

        autor, created = Autor.objects.get_or_create(**autor_data)
        categoria, created = Categoria.objects.get_or_create(**categoria_data)

        livro = Livro.objects.create(autor=autor, categoria=categoria, **validated_data)
        return livro
