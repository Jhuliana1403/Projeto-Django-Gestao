from django.shortcuts import render, redirect, get_object_or_404
from .models import Produtor, Cliente, Coleta, Qualidade, Pagamento, Funcionario, Venda, Transporte
import datetime
from django.core.files.storage import default_storage
from django.contrib import messages
from django.core.exceptions import ValidationError
from datetime import datetime
from django.http import JsonResponse
from django.db.models.functions import TruncMonth
from django.db.models import Sum

def index(request):
    return render(request, 'app/index.html')

def listar_produtor(request):
    produtores = Produtor.objects.all()
    return render(request, 'app/listar_produtor.html', {'produtores': produtores})

def cadastrar_produtor(request):
    storage = messages.get_messages(request)  # Limpa mensagens anteriores para evitar duplicação
    storage.used = True  

    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        fazenda = request.POST.get('fazenda', '').strip()
        localizacao = request.POST.get('localizacao', '').strip()
        telefone = request.POST.get('telefone', '').strip()

        # Validações
        if not nome or not fazenda or not localizacao or not telefone:
            messages.error(request, "Todos os campos são obrigatórios.")
            return render(request, 'app/cadastrar_produtor.html', {
                'nome': nome,
                'fazenda': fazenda,
                'localizacao': localizacao,
                'telefone': telefone
            })

        if not telefone.isdigit() or len(telefone) < 10:
            messages.error(request, "O telefone deve conter apenas números e ter pelo menos 10 dígitos.")
            return render(request, 'app/cadastrar_produtor.html', {
                'nome': nome,
                'fazenda': fazenda,
                'localizacao': localizacao,
                'telefone': telefone
            })

        # Salvar novo produtor
        Produtor.objects.create(nome=nome, fazenda=fazenda, localizacao=localizacao, telefone=telefone)
        messages.success(request, "Produtor cadastrado com sucesso!")
        return redirect('listar_produtor')

    return render(request, 'app/cadastrar_produtor.html')

def editar_produtor(request, produtor_id):
    produtor = get_object_or_404(Produtor, id=produtor_id)

    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        fazenda = request.POST.get('fazenda', '').strip()
        localizacao = request.POST.get('localizacao', '').strip()
        telefone = request.POST.get('telefone', '').strip()

        # Validações
        if not nome or not fazenda or not localizacao or not telefone:
            messages.error(request, "Todos os campos são obrigatórios.")
            return render(request, 'app/editar_produtor.html', {
                'produtor': produtor, 
                'nome': nome, 
                'fazenda': fazenda, 
                'localizacao': localizacao, 
                'telefone': telefone
            })

        if not telefone.isdigit() or len(telefone) < 10:
            messages.error(request, "O telefone deve conter apenas números e ter pelo menos 10 dígitos.")
            return render(request, 'app/editar_produtor.html', {
                'produtor': produtor, 
                'nome': nome, 
                'fazenda': fazenda, 
                'localizacao': localizacao, 
                'telefone': telefone
            })

        produtor.nome = nome
        produtor.fazenda = fazenda
        produtor.localizacao = localizacao
        produtor.telefone = telefone
        produtor.save()
        messages.success(request, "Produtor atualizado com sucesso!")
        return redirect('listar_produtor')

    return render(request, 'app/editar_produtor.html', {'produtor': produtor})

def excluir_produtor(request, produtor_id):
    produtor = get_object_or_404(Produtor, id=produtor_id)
    produtor.delete()
    messages.success(request, "Produtor excluído com sucesso!")
    return redirect('listar_produtor')

def alternar_status_produtor(request, produtor_id):
    produtor = get_object_or_404(Produtor, id=produtor_id)
    produtor.ativo = not produtor.ativo
    produtor.save()
    messages.success(request, "Status do produtor atualizado com sucesso!")
    return redirect('listar_produtor')

# Cliente
def listar_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'app/listar_cliente.html', {'clientes': clientes})

def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        endereco = request.POST.get('endereco', '').strip()
        contato = request.POST.get('contato', '').strip()

        # Validações
        if not nome or not endereco or not contato:
            messages.error(request, "Todos os campos são obrigatórios.")
            return render(request, 'app/cadastrar_cliente.html', {
                'nome': nome,
                'endereco': endereco,
                'contato': contato
            })

        if not contato.isdigit() or len(contato) < 10:
            messages.error(request, "O contato deve conter apenas números e ter pelo menos 10 dígitos.")
            return render(request, 'app/cadastrar_cliente.html', {
                'nome': nome,
                'endereco': endereco,
                'contato': contato
            })

        Cliente.objects.create(nome=nome, endereco=endereco, contato=contato)
        messages.success(request, "Cliente cadastrado com sucesso!")
        return redirect('listar_cliente')

    return render(request, 'app/cadastrar_cliente.html')


def excluir_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    cliente.delete()
    messages.success(request, "Cliente excluído com sucesso!")
    return redirect('listar_cliente')


def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        endereco = request.POST.get('endereco', '').strip()
        contato = request.POST.get('contato', '').strip()

        # Validação dos campos
        if not nome or not endereco or not contato:
            messages.error(request, "Todos os campos são obrigatórios.")
            return render(request, 'app/editar_cliente.html', {'cliente': cliente})

        if not contato.isdigit() or len(contato) < 10:
            messages.error(request, "O contato deve conter apenas números e ter pelo menos 10 dígitos.")
            return render(request, 'app/editar_cliente.html', {'cliente': cliente})

        # Atualiza os dados do cliente
        cliente.nome = nome
        cliente.endereco = endereco
        cliente.contato = contato
        cliente.save()

        messages.success(request, "Cliente atualizado com sucesso!")
        return redirect('listar_cliente')

    return render(request, 'app/editar_cliente.html', {'cliente': cliente})

# Coleta
def listar_coleta(request):
    coletas = Coleta.objects.all()
    return render(request, 'app/listar_coleta.html', {'coletas': coletas})

def cadastrar_coleta(request):
    produtores = Produtor.objects.filter(ativo=True)

    if request.method == "POST":
        produtor_id = request.POST.get("produtor")
        data = request.POST.get("data", "").strip()
        quantidade_litros = request.POST.get("quantidade_litros", "").strip()

        # Valida se todos os campos foram preenchidos
        if not produtor_id or not data or not quantidade_litros:
            messages.error(request, "Todos os campos são obrigatórios.")
            return render(request, "app/cadastrar_coleta.html", {"produtores": produtores})

        # Valida o produtor
        produtor = get_object_or_404(Produtor, id=produtor_id, ativo=True)

        # Valida a quantidade de litros
        try:
            quantidade_litros = float(quantidade_litros)
            if quantidade_litros <= 0:
                raise ValueError
        except ValueError:
            messages.error(request, "Quantidade de litros inválida. Insira um número positivo.")
            return render(request, "app/cadastrar_coleta.html", {"produtores": produtores})

        # Valida a data
        try:
            data_formatada = datetime.strptime(data, "%Y-%m-%d").date()
        except ValueError:
            messages.error(request, "Formato de data inválido. Use AAAA-MM-DD.")
            return render(request, "app/cadastrar_coleta.html", {"produtores": produtores})

        # Cria a coleta
        Coleta.objects.create(produtor=produtor, data=data_formatada, quantidade_litros=quantidade_litros)
        messages.success(request, "Coleta cadastrada com sucesso!")
        return redirect("listar_coleta")

    return render(request, "app/cadastrar_coleta.html", {"produtores": produtores})


def excluir_coleta(request, coleta_id):
    coleta = get_object_or_404(Coleta, id=coleta_id)
    coleta.delete()
    messages.success(request, "Coleta excluída com sucesso!")
    return redirect('listar_coleta')


def editar_coleta(request, coleta_id):
    coleta = get_object_or_404(Coleta, id=coleta_id)
    produtores = Produtor.objects.filter(ativo=True)

    if request.method == 'POST':
        produtor_id = request.POST.get("produtor")
        data = request.POST.get("data", "").strip()
        quantidade_litros = request.POST.get("quantidade_litros", "").strip()

        # Valida se todos os campos foram preenchidos
        if not produtor_id or not data or not quantidade_litros:
            messages.error(request, "Todos os campos são obrigatórios.")
            return render(request, "app/editar_coleta.html", {"coleta": coleta, "produtores": produtores})

        # Valida o produtor
        produtor = get_object_or_404(Produtor, id=produtor_id, ativo=True)

        # Valida a quantidade de litros
        try:
            quantidade_litros = float(quantidade_litros)
            if quantidade_litros <= 0:
                raise ValueError
        except ValueError:
            messages.error(request, "Quantidade de litros inválida. Insira um número positivo.")
            return render(request, "app/editar_coleta.html", {"coleta": coleta, "produtores": produtores})

        # Valida a data
        try:
            data_formatada = datetime.strptime(data, "%Y-%m-%d").date()
        except ValueError:
            messages.error(request, "Formato de data inválido. Use AAAA-MM-DD.")
            return render(request, "app/editar_coleta.html", {"coleta": coleta, "produtores": produtores})

        # Atualiza os dados da coleta
        coleta.produtor = produtor
        coleta.data = data_formatada
        coleta.quantidade_litros = quantidade_litros
        coleta.save()

        messages.success(request, "Coleta atualizada com sucesso!")
        return redirect("listar_coleta")

    return render(request, "app/editar_coleta.html", {"coleta": coleta, "produtores": produtores})

#Qualidade do leite
def listar_qualidade(request):
    qualidade = Qualidade.objects.all()
    return render(request, 'app/listar_qualidade.html', {'qualidade': qualidade})


def cadastrar_qualidade(request):
    if request.method == "POST":
        produtor_id = request.POST.get("produtor")
        coleta_id = request.POST.get("coleta")
        gordura = request.POST.get("gordura")
        proteina = request.POST.get("proteina")
        contagem_bacteriana = request.POST.get("contagem_bacteriana")
        status = request.POST.get("status")

        # Verificar se os campos obrigatórios estão preenchidos
        if not produtor_id or not coleta_id or not gordura or not proteina or not contagem_bacteriana or not status:
            messages.error(request, "Erro: Todos os campos são obrigatórios.")
            return redirect("adicionar_qualidade")

        # Verifica se a coleta já tem um registro de qualidade
        if Qualidade.objects.filter(coleta_id=coleta_id).exists():
            messages.error(request, "Erro: Esta coleta já tem uma qualidade cadastrada.")
            return redirect("app/cadastrar_qualidade")  # Substitua pelo nome correto da sua rota

        # Criar a qualidade se não existir conflito
        try:
            Qualidade.objects.create(
                produtor_id=produtor_id,
                coleta_id=coleta_id,
                gordura=gordura,
                proteina=proteina,
                contagem_bacteriana=contagem_bacteriana,
                status=status,
            )
            messages.success(request, "Qualidade cadastrada com sucesso!")
        except Exception as e:
            messages.error(request, f"Erro ao cadastrar qualidade: {str(e)}")
            return redirect("adicionar_qualidade")

        return redirect("listar_qualidade")

    # Enviar os dados para o template
    produtores = Produtor.objects.all()
    coletas = Coleta.objects.all()
    return render(request, "app/cadastrar_qualidade.html", {"produtores": produtores, "coletas": coletas})


def editar_qualidade(request, qualidade_id):
    qualidade = get_object_or_404(Qualidade, id=qualidade_id)
    produtores = Produtor.objects.all()
    coletas = Coleta.objects.all()

    if request.method == "POST":
        produtor_id = request.POST.get("produtor")
        coleta_id = request.POST.get("coleta")
        gordura = request.POST.get("gordura")
        proteina = request.POST.get("proteina")
        contagem_bacteriana = request.POST.get("contagem_bacteriana")
        status = request.POST.get("status")

        # Verificar se os campos numéricos estão vazios e exibir uma mensagem de erro
        if not gordura or not proteina or not contagem_bacteriana:
            messages.error(request, "Erro: Os campos de gordura, proteína e contagem bacteriana não podem estar vazios.")
            return render(request, "app/editar_qualidade.html", {
                "qualidade": qualidade,
                "produtores": produtores,
                "coletas": coletas
            })

        # Se todos os campos estiverem preenchidos corretamente, salvar os dados
        qualidade.produtor_id = produtor_id
        qualidade.coleta_id = coleta_id
        qualidade.gordura = gordura
        qualidade.proteina = proteina
        qualidade.contagem_bacteriana = contagem_bacteriana
        qualidade.status = status
        qualidade.save()

        messages.success(request, "Qualidade atualizada com sucesso!")
        return redirect("listar_qualidade")

    return render(request, "app/editar_qualidade.html", {
        "qualidade": qualidade,
        "produtores": produtores,
        "coletas": coletas
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
        messages.success(request, "Qualidade excluída com sucesso!")
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

        # Verificação de campos vazios
        if not produtor_id or not data or not valor or not metodo_pagamento:
            messages.error(request, "Todos os campos são obrigatórios. Por favor, preencha todos os campos.")
            return render(request, 'app/cadastrar_pagamento.html', {
                'produtores': Produtor.objects.all(),
                'produtor_id': produtor_id,
                'data': data,
                'valor': valor,
                'metodo_pagamento': metodo_pagamento,
            })

        try:
            # Verifica se o valor pode ser convertido para float
            valor = float(valor)

            # Verifica se o valor é válido
            if valor <= 0:
                messages.error(request, "O valor do pagamento deve ser maior que zero.")
                return render(request, 'app/cadastrar_pagamento.html', {
                    'produtores': Produtor.objects.all(),
                    'produtor_id': produtor_id,
                    'data': data,
                    'valor': valor,
                    'metodo_pagamento': metodo_pagamento,
                })

            produtor = get_object_or_404(Produtor, id=produtor_id)

            # Criação do pagamento
            Pagamento.objects.create(
                produtor=produtor,
                data_pagamento=data,
                valor=valor,
                metodo_pagamento=metodo_pagamento
            )

            messages.success(request, "Pagamento cadastrado com sucesso!")
            return redirect('listar_pagamentos')

        except ValueError:
            messages.error(request, "Erro: O valor do pagamento precisa ser um número válido.")
            return render(request, 'app/cadastrar_pagamento.html', {
                'produtores': Produtor.objects.all(),
                'produtor_id': produtor_id,
                'data': data,
                'valor': valor,
                'metodo_pagamento': metodo_pagamento,
            })

    produtores = Produtor.objects.all()
    return render(request, 'app/cadastrar_pagamento.html', {'produtores': produtores})

def editar_pagamento(request, pagamento_id):
    pagamento = get_object_or_404(Pagamento, id=pagamento_id)

    if request.method == 'POST':
        produtor_id = request.POST.get('produtor')
        data = request.POST.get('data_pagamento')
        valor = request.POST.get('valor')
        metodo_pagamento = request.POST.get('metodo_pagamento')

        # Verificar se algum campo está vazio
        if not produtor_id or not data or not valor or not metodo_pagamento:
            messages.error(request, "Erro: Todos os campos são obrigatórios.")
            return render(request, 'app/editar_pagamento.html', {'pagamento': pagamento, 'produtores': Produtor.objects.all()})

        try:
            valor = float(valor)
            produtor = get_object_or_404(Produtor, id=produtor_id)
            
            # Atualiza o pagamento com as novas informações
            pagamento.produtor = produtor
            pagamento.data_pagamento = data
            pagamento.valor = valor
            pagamento.metodo_pagamento = metodo_pagamento
            pagamento.save()
            
            messages.success(request, "Pagamento editado com sucesso!")
            return redirect('listar_pagamentos')
        except ValueError:
            # Mensagem de erro caso o valor não seja um número válido
            messages.error(request, "Erro: O valor do pagamento precisa ser um número válido.")
            return render(request, 'app/editar_pagamento.html', {'pagamento': pagamento, 'produtores': Produtor.objects.all()})

    produtores = Produtor.objects.all()
    return render(request, 'app/editar_pagamento.html', {'pagamento': pagamento, 'produtores': produtores})

def excluir_pagamento(request, pagamento_id):
    try:
        pagamento = get_object_or_404(Pagamento, id=pagamento_id)
        pagamento.delete()
        messages.success(request, "Pagamento excluído com sucesso!")
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
        imagem = request.FILES.get('imagem')  # Verifica se a imagem foi enviada, caso contrário, None será atribuído

        # Validando os campos obrigatórios
        if not nome or not salario or not funcao or not ativo:
            messages.error(request, 'Todos os campos são obrigatórios, exceto a imagem.')
            return render(request, 'app/cadastrar_funcionario.html')

        # Criação do funcionário
        funcionario = Funcionario(
            nome=nome,
            salario=salario,
            funcao=funcao,
            ativo=ativo,
            imagem=imagem  # Se imagem não for enviada, o valor será None
        )
        
        try:
            funcionario.save()
            messages.success(request, 'Funcionário cadastrado com sucesso!')
        except ValidationError as e:
            messages.error(request, 'Erro ao salvar o funcionário. Verifique os dados e tente novamente.')
        
        return redirect('listar_funcionarios')

    return render(request, 'app/cadastrar_funcionario.html')

def editar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)

    if request.method == "POST":
        funcionario.nome = request.POST['nome']
        funcionario.salario = request.POST['salario']
        funcionario.funcao = request.POST['funcao']
        funcionario.ativo = request.POST['status'] == "Ativo"

        if 'imagem' in request.FILES:
            if funcionario.imagem:
                default_storage.delete(funcionario.imagem.path)  # Deleta a imagem anterior
            funcionario.imagem = request.FILES['imagem']  # Atribui a nova imagem

        try:
            funcionario.save()  # Tenta salvar as alterações
            messages.success(request, 'Funcionário atualizado com sucesso!')
            return redirect('listar_funcionarios')
        except ValidationError as e:
            messages.error(request, 'Erro ao salvar as informações do funcionário. Verifique os dados e tente novamente.')
        
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
    messages.success(request, "Funcionário excluído com sucesso!")
    funcionario.delete()
    return redirect('listar_funcionarios')

# Listar vendas
def listar_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'app/listar_vendas.html', {'vendas': vendas})

def cadastrar_venda(request):
    if request.method == "POST":
        # Obtendo os dados do formulário
        cliente_id = request.POST.get('cliente')
        quantidade_litros = request.POST.get('quantidade_litros')
        valor_total = request.POST.get('valor_total')

        # Verificação de campos vazios
        if not cliente_id or not quantidade_litros or not valor_total:
            messages.error(request, "Todos os campos são obrigatórios. Por favor, preencha todos os campos.")
            return render(request, 'app/cadastrar_venda.html', {
                'clientes': Cliente.objects.all(),
                'cliente_id': cliente_id,
                'quantidade_litros': quantidade_litros,
                'valor_total': valor_total,
            })

        # Validar se o cliente existe
        try:
            cliente = get_object_or_404(Cliente, id=cliente_id)
        except Cliente.DoesNotExist:
            messages.error(request, 'Cliente não encontrado.')
            return render(request, 'app/cadastrar_venda.html', {
                'clientes': Cliente.objects.all(),
                'cliente_id': cliente_id,
                'quantidade_litros': quantidade_litros,
                'valor_total': valor_total,
            })

        # Verificar se os valores de quantidade e valor total são válidos
        try:
            quantidade_litros = float(quantidade_litros)
            valor_total = float(valor_total)

            # Verifica se os valores são válidos (não negativos ou zero)
            if quantidade_litros <= 0 or valor_total <= 0:
                messages.error(request, "A quantidade de litros e o valor total devem ser maiores que zero.")
                return render(request, 'app/cadastrar_venda.html', {
                    'clientes': Cliente.objects.all(),
                    'cliente_id': cliente_id,
                    'quantidade_litros': quantidade_litros,
                    'valor_total': valor_total,
                })

        except ValueError:
            messages.error(request, "A quantidade de litros e o valor total precisam ser números válidos.")
            return render(request, 'app/cadastrar_venda.html', {
                'clientes': Cliente.objects.all(),
                'cliente_id': cliente_id,
                'quantidade_litros': quantidade_litros,
                'valor_total': valor_total,
            })

        # Criando a venda
        Venda.objects.create(
            cliente=cliente,
            quantidade_litros=quantidade_litros,
            valor_total=valor_total
        )

        messages.success(request, 'Venda cadastrada com sucesso!')
        return redirect('listar_vendas')

    clientes = Cliente.objects.all()
    return render(request, 'app/cadastrar_venda.html', {'clientes': clientes})

def editar_venda(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)
    
    if request.method == "POST":
        # Obter os dados do formulário
        cliente_id = request.POST.get('cliente')
        quantidade_litros = request.POST.get('quantidade_litros')
        valor_total = request.POST.get('valor_total')

        # Validação dos campos
        if not cliente_id or not quantidade_litros or not valor_total:
            messages.error(request, "Todos os campos são obrigatórios.")
            return render(request, 'app/editar_venda.html', {
                'venda': venda,
                'clientes': Cliente.objects.all(),
            })

        try:
            quantidade_litros = float(quantidade_litros)
            valor_total = float(valor_total)
        except ValueError:
            messages.error(request, "A quantidade de litros e o valor total devem ser números válidos.")
            return render(request, 'app/editar_venda.html', {
                'venda': venda,
                'clientes': Cliente.objects.all(),
            })

        # Atualizar a venda com os dados válidos
        venda.cliente_id = cliente_id
        venda.quantidade_litros = quantidade_litros
        venda.valor_total = valor_total
        venda.save()

        # Mensagem de sucesso
        messages.success(request, "Venda atualizada com sucesso.")
        return redirect('listar_vendas')

    clientes = Cliente.objects.all()
    return render(request, 'app/editar_venda.html', {'venda': venda, 'clientes': clientes})

# Excluir venda
def excluir_venda(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)
    messages.success(request, "Venda excluída com sucesso.")
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

def listar_transporte(request):
    transportes = Transporte.objects.all()
    return render(request, 'app/listar_transporte.html', {'transportes': transportes})

def cadastrar_transporte(request):
    if request.method == "POST":
        motorista = request.POST.get("motorista")
        placa = request.POST.get("placa")
        coleta_quantidade = request.POST.get("coleta_quantidade")
        destino = request.POST.get("destino")
        data_envio = request.POST.get("data_envio")
        status = request.POST.get("status")
        motivo_atraso = request.POST.get("motivo_atraso", "")
        feedback_cliente = request.POST.get("feedback_cliente", "")

        # Verificação para garantir que a placa seja única
        if Transporte.objects.filter(placa=placa).exists():
            messages.error(request, "A placa informada já está cadastrada. Por favor, insira uma placa única.")
            transportes = Transporte.objects.all()  # Recupera os transportes já cadastrados
            return render(request, "app/cadastrar_transporte.html", {
                "transportes": transportes,
                "motorista": motorista,
                "placa": placa,
                "coleta_quantidade": coleta_quantidade,
                "destino": destino,
                "data_envio": data_envio,
                "status": status,
                "motivo_atraso": motivo_atraso,
                "feedback_cliente": feedback_cliente
            })

        # Validação de campos obrigatórios
        if not motorista or not placa or not coleta_quantidade or not destino or not status:
            messages.error(request, "Por favor, preencha todos os campos obrigatórios.")
            transportes = Transporte.objects.all()  # Recupera os transportes já cadastrados
            return render(request, "app/cadastrar_transporte.html", {
                "transportes": transportes,
                "motorista": motorista,
                "placa": placa,
                "coleta_quantidade": coleta_quantidade,
                "destino": destino,
                "data_envio": data_envio,
                "status": status,
                "motivo_atraso": motivo_atraso,
                "feedback_cliente": feedback_cliente
            })

        # Se todos os campos obrigatórios estão preenchidos, cria o transporte
        transporte = Transporte(
            motorista=motorista,
            placa=placa,
            coleta_quantidade=coleta_quantidade,
            destino=destino,
            data_envio=data_envio,
            status=status,
            motivo_atraso=motivo_atraso,
            feedback_cliente=feedback_cliente
        )
        transporte.save()
        return redirect("listar_transporte")

    # Caso o método não seja POST, exibe o formulário para cadastrar transporte
    transportes = Transporte.objects.all()  # Recupera todos os transportes existentes
    return render(request, "app/cadastrar_transporte.html", {"transportes": transportes})



def editar_transporte(request, transporte_id):
    transporte = get_object_or_404(Transporte, id=transporte_id)

    if request.method == "POST":
        # Pegando os valores do formulário
        motorista = request.POST.get("motorista", transporte.motorista)
        placa = request.POST.get("placa", transporte.placa)
        coleta_quantidade = request.POST.get("coleta_quantidade", transporte.coleta_quantidade)
        destino = request.POST.get("destino", transporte.destino)
        data_envio = request.POST.get("data_envio")
        status = request.POST.get("status", transporte.status)
        motivo_atraso = request.POST.get("motivo_atraso", transporte.motivo_atraso)
        feedback_cliente = request.POST.get("feedback_cliente", transporte.feedback_cliente)

        # Validação: Verificar se campos obrigatórios estão vazios
        if not motorista or not placa or not destino or not data_envio:
            messages.error(request, "Os campos 'Motorista', 'Placa', 'Destino' e 'Data de Envio' são obrigatórios.")
            return render(request, "app/editar_transporte.html", {"transporte": transporte})

        # Validação: Verificar se o campo 'coleta_quantidade' é um número decimal
        if coleta_quantidade:
            try:
                coleta_quantidade = float(coleta_quantidade)  # Tenta converter para decimal
            except ValueError:
                messages.error(request, "O campo 'Coleta' deve ser um número decimal válido.")
                return render(request, "app/editar_transporte.html", {"transporte": transporte})
        else:
            coleta_quantidade = 0  # Definindo um valor padrão caso o campo esteja vazio

        # Atualizando os valores no transporte
        transporte.motorista = motorista
        transporte.placa = placa
        transporte.coleta_quantidade = coleta_quantidade
        transporte.destino = destino
        transporte.data_envio = data_envio
        transporte.status = status
        transporte.motivo_atraso = motivo_atraso
        transporte.feedback_cliente = feedback_cliente

        # Salvando o transporte
        transporte.save()
        messages.success(request, "Transporte atualizado com sucesso!")
        return redirect("listar_transporte")  # Redireciona após salvar

    return render(request, "app/editar_transporte.html", {"transporte": transporte})

def excluir_transporte(request, transporte_id):
    transporte = get_object_or_404(Transporte, id=transporte_id)
    messages.success(request, "Transporte excluído com sucesso!")
    transporte.delete()
    return redirect('listar_transporte')