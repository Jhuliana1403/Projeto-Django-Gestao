from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .forms import AdminCreationForm

# Create your views here.

#Tela de login 
def index(request):
    if request.method == "GET":
        return render(request, 'login/index.html')
    else:        
        email = request.POST.get('email')
        senha = request.POST.get('password')

        user = authenticate(username=email, password=senha)

        if user:
            login(request, user)
            return render(request, 'app/dashboard.html')
        else:
            return render(request, "login/index.html", {"erro": "Email ou senha incorreto!"})
        

def sair(request):
    logout(request)
    return redirect('login_index')

# Verifica se o usuário é admin antes de acessar a página
def is_admin(user):
    return user.is_staff  # Somente usuários com permissão de staff (admin)

@user_passes_test(is_admin)  # Apenas admins podem acessar
def cadastrar_admin(request):
    if request.method == 'POST':
        form = AdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Novo administrador cadastrado com sucesso!")
            return redirect('cadastrar_admin')  # Redireciona para a mesma página ou outra
    else:
        form = AdminCreationForm()

    return render(request, 'login/cadastrar_admin.html', {'form': form})