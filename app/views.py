from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

def index(request):
    return render(request, 'app/index.html')

def cadastrar_produto(request):
    if request.method == 'POST':
        nome_produto = request.POST.get('nome', '').strip()
        descricao_produto = request.POST.get('descricao', '').strip()
        valor_produto = request.POST.get('valor', '').strip()
        quantidade = request.POST.get('quantidade', '').strip()
        try:
            valor_produto = float(valor_produto)  # Convertendo para número decimal
            quantidade = int(quantidade)  # Convertendo para inteiro
        except ValueError:
            return render(request, 'app/cadastrar_produto.html', {'erro': 'Valores inválidos'})

        if nome_produto and descricao_produto:
            post_cadastro = Produto(
                nome=nome_produto,
                descricao=descricao_produto,
                valor=valor_produto,
                quantidade_inicial=quantidade,
                quantidade_final=quantidade  # Inicializando com o mesmo valor
            )
            post_cadastro.save()
            return redirect('listar_produto')  # Redireciona após salvar

    return render(request, 'app/cadastrar_produto.html')

def listar_produtos(request):
    produtos = Produto.objects.all()  # Busca todos os produtos
    return render(request, 'app/listar_produtos.html', {'produtos': produtos})

def excluir_produto(request, produto_id):
    try:
        produto = Produto.objects.get(id=produto_id)
        produto.delete()
        return redirect('listar_produto')  # Nome deve ser igual ao urls.py
    except Produto.DoesNotExist:
        return render(request, 'app/listar_produtos.html', {'erro': 'Produto não encontrado'})


def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        produto.nome = request.POST.get('nome', '').strip()
        produto.descricao = request.POST.get('descricao', '').strip()
        produto.valor = request.POST.get('valor', '').strip()
        produto.quantidade_inicial = request.POST.get('quantidade', '').strip()
        
        try:
            produto.valor = float(produto.valor)
            produto.quantidade_inicial = int(produto.quantidade_inicial)
        except ValueError:
            return render(request, 'app/editar_produto.html', {'produto': produto, 'erro': 'Valores inválidos'})

        produto.save()
        return redirect('listar_produto')

    return render(request, 'app/editar_produto.html', {'produto': produto})