from django.shortcuts import render, redirect, get_object_or_404
from .models import Produtor, Cliente, Coleta, Qualidade, Pagamento, Venda
from datetime import datetime

def index(request):
    return render(request, 'app/index.html')

# Produtor
def listar_produtor(request):
    produtores = Produtor.objects.all()
    return render(request, 'app/listar_produtor.html', {'produtores': produtores})

def cadastrar_produtor(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        fazenda = request.POST.get('fazenda', '').strip()
        localizacao = request.POST.get('localizacao', '').strip()
        telefone = request.POST.get('telefone', '').strip()
        if nome and fazenda and localizacao and telefone:
            Produtor.objects.create(nome=nome, fazenda=fazenda, localizacao=localizacao, telefone=telefone)
            return redirect('listar_produtor')
    return render(request, 'app/cadastrar_produtor.html')

def excluir_produtor(request, produtor_id):
    try:
        produtor = Produtor.objects.get(id=produtor_id)
        produtor.delete()
        return redirect('listar_produtor')  # Nome deve ser igual ao urls.py
    except Produtor.DoesNotExist:
        return render(request, 'app/listar_produtor.html', {'erro': 'Produtor não encontrado'})


def editar_produtor(request, produtor_id):
    produtor = get_object_or_404(Produtor, id=produtor_id)

    if request.method == 'POST':
        produtor.nome = request.POST.get('nome', '').strip()
        produtor.fazenda = request.POST.get('fazenda', '').strip()
        produtor.localizacao = request.POST.get('localizacao', '').strip()
        produtor.telefone = request.POST.get('telefone', '').strip()

        produtor.save()
        return redirect('listar_produtor')

    return render(request, 'app/editar_produtor.html', {'produtor': produtor})


def alternar_status_produtor(request, produtor_id):
    produtor = get_object_or_404(Produtor, id=produtor_id)
    produtor.ativo = not produtor.ativo  # Alterna entre True e False
    produtor.save()
    return redirect('listar_produtor')  # Redireciona para a lista de produtores

# Cliente
def listar_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'app/listar_cliente.html', {'clientes': clientes})

def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        endereco = request.POST.get('endereco', '').strip()
        contato = request.POST.get('contato', '').strip()
        if nome and endereco and contato:
            Cliente.objects.create(nome=nome, endereco=endereco, contato=contato)
            return redirect('listar_cliente')
    return render(request, 'app/cadastrar_cliente.html')

def excluir_cliente(request, cliente_id):
    try:
        cliente = Cliente.objects.get(id=cliente_id)
        cliente.delete()
        return redirect('listar_cliente') 
    except Cliente.DoesNotExist:
        return render(request, 'app/listar_cliente.html', {'erro': 'Cliente não encontrado'})


def editar_cliente(request, cliente_id):
    clientes = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        clientes.nome = request.POST.get('nome', '').strip()
        clientes.endereco = request.POST.get('endereco', '').strip()
        clientes.contato = request.POST.get('contato', '').strip()

        clientes.save()
        return redirect('listar_cliente')

    return render(request, 'app/editar_cliente.html', {'clientes': clientes})

# Coleta
def listar_coleta(request):
    coletas = Coleta.objects.all()
    return render(request, 'app/listar_coleta.html', {'coletas': coletas})

def cadastrar_coleta(request):
    produtores = Produtor.objects.filter(ativo=True)  # Apenas produtores ativos

    if request.method == 'POST':
        produtor_id = request.POST.get('produtor', '').strip()
        data = request.POST.get('data', '').strip()
        quantidade_litros = request.POST.get('quantidade_litros', '').strip()

        if produtor_id and data and quantidade_litros:
            try:
                # Obtém o produtor ativo do banco de dados
                produtor = get_object_or_404(Produtor, id=produtor_id, ativo=True)

                # Converte a quantidade de litros para decimal
                quantidade_litros = float(quantidade_litros)

                # Converte a data para o formato correto
                data_formatada = datetime.strptime(data, "%Y-%m-%d")

                # Cria a coleta
                Coleta.objects.create(produtor=produtor, data=data_formatada, quantidade_litros=quantidade_litros)

                return redirect('listar_coleta')

            except ValueError:
                return render(request, 'app/cadastrar_coleta.html', {
                    'produtores': produtores,
                    'erro': 'Quantidade inválida'
                })

    return render(request, 'app/cadastrar_coleta.html', {'produtores': produtores})


def excluir_coleta(request, coleta_id):
    try:
        coleta = Coleta.objects.get(id=coleta_id)
        coleta.delete()
        return redirect('listar_coleta') 
    except Coleta.DoesNotExist:
        return render(request, 'app/listar_coleta.html', {'erro': 'Coleta não encontrado'})
    
def editar_coleta(request, coleta_id):
    coleta = get_object_or_404(Coleta, id=coleta_id)
    produtores = Produtor.objects.filter(ativo=True)  # Apenas produtores ativos

    if request.method == 'POST':
        produtor_id = request.POST.get('produtor', '').strip()
        data = request.POST.get('data', '').strip()
        quantidade_litros = request.POST.get('quantidade_litros', '').strip()

        if produtor_id and data and quantidade_litros:
            try:
                # Obtém o produtor ativo do banco de dados
                produtor = get_object_or_404(Produtor, id=produtor_id, ativo=True)
                
                # Converte a quantidade de litros para decimal
                quantidade_litros = float(quantidade_litros)

                # Converte a data para o formato correto
                data_formatada = datetime.strptime(data, "%Y-%m-%d")

                # Atualiza os campos da coleta
                coleta.produtor = produtor
                coleta.data = data_formatada
                coleta.quantidade_litros = quantidade_litros

                # Salva a coleta no banco de dados
                coleta.save()

                return redirect('listar_coleta')

            except ValueError:
                return render(request, 'app/editar_coleta.html', {
                    'coleta': coleta,
                    'produtores': produtores,
                    'erro': 'Quantidade inválida'
                })

    return render(request, 'app/editar_coleta.html', {'coleta': coleta, 'produtores': produtores})

# Pagamento
def listar_pagamentos(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'app/listar_pagamentos.html', {'pagamentos': pagamentos})

def cadastrar_pagamento(request):
    if request.method == 'POST':
        produtor_id = request.POST.get('produtor')
        valor = request.POST.get('valor')
        metodo_pagamento = request.POST.get('metodo_pagamento')
        produtor = get_object_or_404(Produtor, id=produtor_id)
        try:
            valor = float(valor)
            Pagamento.objects.create(produtor=produtor, valor=valor, metodo_pagamento=metodo_pagamento)
            return redirect('listar_pagamentos')
        except ValueError:
            return render(request, 'app/cadastrar_pagamento.html', {'erro': 'Valor inválido'})
    produtores = Produtor.objects.all()
    return render(request, 'app/cadastrar_pagamento.html', {'produtores': produtores})

# Venda
def listar_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'app/listar_vendas.html', {'vendas': vendas})

def cadastrar_venda(request):
    if request.method == 'POST':
        fornecedor_id = request.POST.get('fornecedor')
        quantidade_litros = request.POST.get('quantidade_litros')
        valor_total = request.POST.get('valor_total')
        fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
        try:
            quantidade_litros = float(quantidade_litros)
            valor_total = float(valor_total)
            Venda.objects.create(fornecedor=fornecedor, quantidade_litros=quantidade_litros, valor_total=valor_total)
            return redirect('listar_vendas')
        except ValueError:
            return render(request, 'app/cadastrar_venda.html', {'erro': 'Valores inválidos'})
    fornecedores = Fornecedor.objects.all()
    return render(request, 'app/cadastrar_venda.html', {'fornecedores': fornecedores})

# Transporte
def listar_transportes(request):
    transportes = Transporte.objects.all()
    return render(request, 'app/listar_transportes.html', {'transportes': transportes})

def cadastrar_transporte(request):
    if request.method == 'POST':
        venda_id = request.POST.get('venda')
        motorista = request.POST.get('motorista')
        placa_veiculo = request.POST.get('placa_veiculo')
        data_envio = request.POST.get('data_envio')
        venda = get_object_or_404(Venda, id=venda_id)
        Transporte.objects.create(venda=venda, motorista=motorista, placa_veiculo=placa_veiculo, data_envio=data_envio)
        return redirect('listar_transportes')
    vendas = Venda.objects.all()
    return render(request, 'app/cadastrar_transporte.html', {'vendas': vendas})