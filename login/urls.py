from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login_index'),
    path('cadastrar_admin/', views.cadastrar_admin, name='cadastrar_admin')
]
