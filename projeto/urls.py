from django.contrib import admin
from django.urls import path, include
from login import views as views_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('login/', include('login.urls')),
    path('logout/', views_login.sair, name='logout'),
]
