from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login_index'),
    path('cadastrar_admin/', views.cadastrar_admin, name='cadastrar_admin'),
    path('editar_admin/', views.editar_admin, name='editar_admin'),
    path('visualizar_admin/', views.visualizar_admin, name='visualizar_admin'),
]
