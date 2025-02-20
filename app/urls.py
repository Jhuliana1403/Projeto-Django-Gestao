from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # Rotas para Produtor
    path("cadastrar_produtor/", views.cadastrar_produtor, name="cadastrar_produtor"),
    path("listar_produtor/", views.listar_produtor, name="listar_produtor"),
    path('editar_produtor/<int:produtor_id>/', views.editar_produtor, name='editar_produtor'),
    path('excluir_produtor/<int:produtor_id>/', views.excluir_produtor, name='excluir_produtor'),
    path('alternar-status/<int:produtor_id>/', views.alternar_status_produtor, name='alternar_status_produtor'),


    # Rotas para Cliente
    path("cadastrar_cliente/", views.cadastrar_cliente, name="cadastrar_cliente"),
    path("listar_cliente/", views.listar_cliente, name="listar_cliente"),
    path('editar_cliente/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('excluir_cliente/<int:cliente_id>/', views.excluir_cliente, name='excluir_cliente'),

    # Rotas para Coleta
    path("cadastrar_coleta/", views.cadastrar_coleta, name="cadastrar_coleta"),
    path("listar_coleta/", views.listar_coleta, name="listar_coleta"),
    path('editar_coleta/<int:coleta_id>/', views.editar_coleta, name='editar_coleta'),
    path('excluir_coleta/<int:coleta_id>/', views.excluir_coleta, name='excluir_coleta'),

    # # Rotas para Colaborador
    # path("cadastrar_col/", views.cadastrar_colaborador, name="cadastrar_colaborador"),
    # path("listar_col/", views.listar_colaborador, name="listar_colaborador"),
    # # path('editar_col/<int:col_id>/', views.editar_colaborador, name='editar_colaborador'),
    # path('col_desativar/<int:id>/', views.desativar_colaborador, name='desativar_colaborador'),
    # path('excluir_col/<int:col_id>/', views.excluir_colaborador, name='excluir_colaborador'),
]
