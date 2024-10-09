from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)
    publicado_em = models.DateField()

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


