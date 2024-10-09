from django.urls import path
from .views import LivroList, LivroDetail

urlpatterns = [
    path('livros/', LivroList.as_view(), name='livros-list'),
    path('livros/<int:pk>/', LivroDetail.as_view(), name='livro-detail'),
]
