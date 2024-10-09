from django.core.management.base import BaseCommand
from core.models import Autor, Categoria, Livro  # Ajuste o import conforme seu projeto

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados de teste'

    def handle(self, *args, **kwargs):
        # Criação de algumas categorias
        categoria1 = Categoria.objects.create(nome='Ficção')
        categoria2 = Categoria.objects.create(nome='Não-ficção')

        # Criação de alguns autores
        autor1 = Autor.objects.create(nome='Autor 1', email='autor1@email.com')
        autor2 = Autor.objects.create(nome='Autor 2', email='autor2@email.com')

        # Criação de alguns livros
        Livro.objects.create(titulo='Livro 1', autor=autor1, categoria=categoria1, publicado_em='2024-01-01')
        Livro.objects.create(titulo='Livro 2', autor=autor2, categoria=categoria2, publicado_em='2024-02-01')

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))
