from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastrar/", views.cadastrar_produto, name="cadastrar_produto"),
    path("listar_produto/", views.listar_produtos, name="listar_produto"),
    path('excluir/<int:produto_id>/', views.excluir_produto, name='excluir_produto'),
    path('editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
]