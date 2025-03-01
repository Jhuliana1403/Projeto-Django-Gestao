from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Dashboard
    path("", views.dashboard, name="dashboard"),

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

    # Rotas para Qualidade 
    path('qualidade_leite/', views.listar_qualidade, name='listar_qualidade'),
    path('adicionar_qualidade/', views.cadastrar_qualidade, name='adicionar_qualidade'),
    path('editar_qualidade/<int:qualidade_id>/', views.editar_qualidade, name='editar_qualidade'),
    path('exluir_qualidade/<int:qualidade_id>/', views.excluir_qualidade, name='excluir_qualidade'),
    path('obter_coletas/', views.obter_coletas, name='obter_coletas'),
    path('alternar-status_qualidade/<int:qualidade_id>/', views.alternar_status_qualidade, name='alternar_status_qualidade'),

    #Rotas para Pagamento de produtores
    path('pagamentos/', views.listar_pagamentos, name='listar_pagamentos'),
    path('cadastrar_pagamentos/', views.cadastrar_pagamento, name='cadastrar_pagamento'),
    path('editar_pagamentos/<int:pagamento_id>/', views.editar_pagamento, name='editar_pagamento'),
    path('excluir_pagamentos/<int:pagamento_id>/', views.excluir_pagamento, name='excluir_pagamento'),

    #Rotas para Funcionários
    path('funcionarios/', views.listar_funcionarios, name="listar_funcionarios"),
    path('cadastrar_funcionarios/', views.cadastrar_funcionario, name="cadastrar_funcionario"),
    path('editar_funcionarios/<int:funcionario_id>/', views.editar_funcionario, name="editar_funcionario"),
    path('alternar_status_funcionarios/<int:funcionario_id>/', views.alternar_status_funcionario, name="alternar_status_funcionario"),
    path('excluir_funcionarios/<int:funcionario_id>/', views.excluir_funcionario, name="excluir_funcionario"),

    #Rotas para Vendas
    path('vendas/', views.listar_vendas, name='listar_vendas'),
    path('cadastrar_venda/', views.cadastrar_venda, name='cadastrar_venda'),
    path('editar_venda/<int:venda_id>/', views.editar_venda, name='editar_venda'),
    path('excluir_venda/<int:venda_id>/', views.excluir_venda, name='excluir_venda'),

    #Rotas para Transporte
    path('transportes/', views.listar_transporte, name='listar_transporte'),
    path('cadastrar_transporte/', views.cadastrar_transporte, name="cadastrar_transporte"),
    path("editar_transporte/<int:transporte_id>/", views.editar_transporte, name="editar_transporte"),
    path("excluir_transporte/<int:transporte_id>/", views.excluir_transporte, name="excluir_transporte"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)