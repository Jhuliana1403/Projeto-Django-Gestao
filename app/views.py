from django.shortcuts import render, redirect, get_object_or_404
from .models import Produtor, Cliente, Coleta, Qualidade, Pagamento, Funcionario, Venda
from datetime import datetime
from django.core.files.storage import default_storage

#Importando para realizar os gráficos
from datetime import datetime
from django.http import JsonResponse
from django.db.models.functions import TruncMonth, TruncYear
from django.db.models import Sum

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

#Qualidade do leite
def listar_qualidade(request):
    qualidade = Qualidade.objects.all()
    return render(request, 'app/listar_qualidade.html', {'qualidade': qualidade})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Produtor, Coleta, Qualidade

def adicionar_qualidade(request):
    produtores = Produtor.objects.filter(ativo=True)  # Apenas produtores ativos
    coletas_disponiveis = Coleta.objects.filter(qualidade__isnull=True)  # Coletas sem qualidade

    if request.method == 'POST':
        coleta_id = request.POST.get('coleta')
        gordura = request.POST.get('gordura')
        proteina = request.POST.get('proteina')
        contagem_bacteriana = request.POST.get('contagem_bacteriana')
        status = request.POST.get('status')

        if coleta_id and gordura and proteina and contagem_bacteriana and status:
            coleta = get_object_or_404(Coleta, id=coleta_id)

            qualidade = Qualidade(
                coleta=coleta,
                gordura=float(gordura),
                proteina=float(proteina),
                contagem_bacteriana=float(contagem_bacteriana),
                status=status,
            )
            qualidade.save()
            return redirect('listar_qualidade')

    return render(request, 'app/cadastrar_qualidade.html', {
        'produtores': produtores,
        'coletas': coletas_disponiveis
    })


def editar_qualidade(request, qualidade_id):
    qualidade = get_object_or_404(Qualidade, id=qualidade_id)
    produtores = Produtor.objects.filter(ativo=True)  # Apenas produtores ativos
    coletas = Coleta.objects.filter(produtor=qualidade.produtor)  # Filtra coletas do produtor

    if request.method == 'POST':
        produtor_id = request.POST.get('produtor')
        coleta_id = request.POST.get('coleta')
    
        if produtor_id:
            qualidade.produtor_id = int(produtor_id)

        if coleta_id:
            qualidade.coleta_id = int(coleta_id)

        qualidade.gordura = float(request.POST.get('gordura', 0))
        qualidade.proteina = float(request.POST.get('proteina', 0))
        qualidade.contagem_bacteriana = int(request.POST.get('contagem_bacteriana', 0))
        qualidade.status = request.POST.get('status')

        qualidade.save()
        return redirect('listar_qualidade')

    return render(request, 'app/editar_qualidade.html', {
        'qualidade': qualidade,
        'produtores': produtores,
        'coletas': coletas
    })


def obter_coletas(request):
    produtor_id = request.GET.get('produtor_id')

    if produtor_id:
        coletas = Coleta.objects.filter(produtor_id=produtor_id).values('id', 'quantidade_litros')
        return JsonResponse(list(coletas), safe=False)
    
    return JsonResponse({"error": "ID do produtor não fornecido"}, status=400)

def excluir_qualidade(request, qualidade_id):
    try:
        qualidade = Qualidade.objects.get(id=qualidade_id)
        qualidade.delete()
        return redirect('listar_qualidade') 
    except Qualidade.DoesNotExist:
        return render(request, 'app/listar_qualidade.html', {'erro': 'Qualidade não encontrado'})

def alternar_status_qualidade(request, qualidade_id):
    qualidade = get_object_or_404(Qualidade, id=qualidade_id)
    qualidade.ativo = not qualidade.ativo  # Alterna entre True e False
    qualidade.save()
    return redirect('listar_qualidade')  # Redireciona para a lista de qualidade


# Pagamento
def listar_pagamentos(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'app/listar_pagamentos.html', {'pagamentos': pagamentos})

def cadastrar_pagamento(request):
    if request.method == 'POST':
        produtor_id = request.POST.get('produtor')
        data = request.POST.get('data_pagamento')
        valor = request.POST.get('valor')
        metodo_pagamento = request.POST.get('metodo_pagamento')
        produtor = get_object_or_404(Produtor, id=produtor_id)
        try:
            valor = float(valor)
            Pagamento.objects.create(produtor=produtor, data_pagamento = data, valor=valor, metodo_pagamento=metodo_pagamento)
            return redirect('listar_pagamentos')
        except ValueError:
            return render(request, 'app/cadastrar_pagamento.html', {'erro': 'Valor inválido'})
    produtores = Produtor.objects.all()
    return render(request, 'app/cadastrar_pagamento.html', {'produtores': produtores})

def editar_pagamento(request, pagamento_id):
    pagamento = get_object_or_404(Pagamento, id=pagamento_id)
    
    if request.method == 'POST':
        produtor_id = request.POST.get('produtor')
        data = request.POST.get('data_pagamento')
        valor = request.POST.get('valor')
        metodo_pagamento = request.POST.get('metodo_pagamento')

        try:
            valor = float(valor)
            produtor = get_object_or_404(Produtor, id=produtor_id)
            
            pagamento.produtor = produtor
            pagamento.data_pagamento = data
            pagamento.valor = valor
            pagamento.metodo_pagamento = metodo_pagamento
            pagamento.save()
            
            return redirect('listar_pagamentos')
        except ValueError:
            return render(request, 'app/editar_pagamento.html', {'pagamento': pagamento, 'erro': 'Valor inválido'})

    produtores = Produtor.objects.all()
    return render(request, 'app/editar_pagamento.html', {'pagamento': pagamento, 'produtores': produtores})


def excluir_pagamento(request, pagamento_id):
    try:
        pagamento = get_object_or_404(Pagamento, id=pagamento_id)
        pagamento.delete()
        return redirect('listar_pagamentos')  # Redireciona para a lista de pagamentos
    except Pagamento.DoesNotExist:
        return render(request, 'app/listar_pagamentos.html', {'erro': 'Pagamento não encontrado'})
    
# Listar funcionários
def listar_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'app/listar_funcionarios.html', {'funcionarios': funcionarios})

# Cadastrar funcionário
def cadastrar_funcionario(request):
    if request.method == "POST":
        nome = request.POST['nome']
        salario = request.POST['salario']
        funcao = request.POST['funcao']
        ativo = request.POST['status'] == "Ativo"
        imagem = request.FILES.get('imagem')

        funcionario = Funcionario(
            nome=nome,
            salario=salario,
            funcao=funcao,
            ativo=ativo,
            imagem=imagem
        )
        funcionario.save()
        return redirect('listar_funcionarios')

    return render(request, 'app/cadastrar_funcionario.html')

# Editar funcionário
def editar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)

    if request.method == "POST":
        funcionario.nome = request.POST['nome']
        funcionario.salario = request.POST['salario']
        funcionario.funcao = request.POST['funcao']
        funcionario.ativo = request.POST['status'] == "Ativo"

        if 'imagem' in request.FILES:
            if funcionario.imagem:
                default_storage.delete(funcionario.imagem.path)
            funcionario.imagem = request.FILES['imagem']

        funcionario.save()
        return redirect('listar_funcionarios')

    return render(request, 'app/editar_funcionario.html', {'funcionario': funcionario})

# Alternar status (Ativo/Inativo)
def alternar_status_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    funcionario.ativo = not funcionario.ativo
    funcionario.save()
    return redirect('listar_funcionarios')

# Excluir funcionário
def excluir_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    if funcionario.imagem:
        default_storage.delete(funcionario.imagem.path)
    funcionario.delete()
    return redirect('listar_funcionarios')

#Vendas
# Listar vendas
def listar_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'app/listar_vendas.html', {'vendas': vendas})

# Cadastrar venda
def cadastrar_venda(request):
    if request.method == "POST":
        cliente_id = request.POST['cliente']
        quantidade_litros = request.POST['quantidade_litros']
        valor_total = request.POST['valor_total']

        cliente = get_object_or_404(Cliente, id=cliente_id)

        venda = Venda(
            cliente=cliente,
            quantidade_litros=quantidade_litros,
            valor_total=valor_total
        )
        venda.save()
        return redirect('listar_vendas')

    clientes = Cliente.objects.all()
    return render(request, 'app/cadastrar_venda.html', {'clientes': clientes})

# Editar venda
def editar_venda(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)

    if request.method == "POST":
        venda.cliente_id = request.POST['cliente']
        venda.quantidade_litros = request.POST['quantidade_litros']
        venda.valor_total = request.POST['valor_total']
        venda.save()
        return redirect('listar_vendas')

    clientes = Cliente.objects.all()
    return render(request, 'app/editar_venda.html', {'venda': venda, 'clientes': clientes})

# Excluir venda
def excluir_venda(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)
    venda.delete()
    return redirect('listar_vendas')

def dashboard(request):
    hoje = datetime.today()
    mes_atual = hoje.strftime("%B")
    ano_atual = hoje.year

    total_salarios = Funcionario.objects.aggregate(total=Sum('salario'))['total'] or 0
    total_pagamentos = Pagamento.objects.aggregate(total=Sum('valor'))['total'] or 0

    # Dados para o gráfico de salários
    funcionarios = Funcionario.objects.values('nome', 'salario')
    nomes_funcionarios = [f['nome'] for f in funcionarios]
    salarios_funcionarios = [f['salario'] for f in funcionarios]

    # Pagamentos Mensais
    pagamentos_mensais = (
        Pagamento.objects
        .annotate(mes=TruncMonth('data_pagamento'))
        .values('mes')
        .annotate(total=Sum('valor'))
        .order_by('mes')
    )
    meses = [p['mes'].strftime("%b/%Y") if p['mes'] else "Data Indefinida" for p in pagamentos_mensais]
    valores_mensais = [p['total'] for p in pagamentos_mensais]

    return render(request, 'app/dashboard.html', {
        'mes_atual': mes_atual,
        'ano_atual': ano_atual,
        'total_salarios': total_salarios,
        'total_pagamentos': total_pagamentos,
        'meses': meses,
        'valores_mensais': valores_mensais,
        'nomes_funcionarios': nomes_funcionarios,
        'salarios_funcionarios': salarios_funcionarios
    })