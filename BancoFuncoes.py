saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas_correntes = 1
AGENCIA = '0001'

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f'Depositado R${valor}')
        print('Deposito feito com sucesso.')
        return saldo, extrato
    else:
        print('Valor inválido.')

def sacar(saldo, valor, extrato, limite, n_saques):
    if valor > limite:
        return 'Você não pode sacar mais que R$500.'
    elif valor > saldo:
        return 'Saldo insuficiente.'
    else:
        saldo -= valor
        extrato.append(f'Saque de R${valor}')
        print('Saque feito com sucesso.')
        n_saques += 1
        return saldo, extrato, n_saques
    
def criarUsuario(dados_usuario, usuarios):
    usuarios.append(dados_usuario)
    print('Usuário registrado com sucesso.')
    return usuarios

def verificarCPF(usuarios, cpf):
    if len(usuarios) < 1:
        return True
    for p in usuarios:
        if p['cpf'] != int(cpf):
            return True
        else:
            return False

def criarConta(agencia, numero_conta, cpf, usuarios):
    for p in usuarios:
        if p['cpf'] == int(cpf):
            p['contas'].append({'agencia': agencia, 'numero_conta': numero_conta})
    return usuarios, numero_conta+1
while True:
    print(''' 
          ========== BANCO ============
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar usuário
[l] Listar usuários
[c] Criar conta corrente
[q] Sair
''')
    opcao = input('=> ')

    if opcao == 'd':
        valor = float(input('Quanto deseja depositar? '))
        saldo, extrato = depositar(saldo, valor, extrato)
        
    if opcao == 's':
        if numero_saques < LIMITE_SAQUES:
            valor = float(input('Quanto deseja sacar? '))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                n_saques=numero_saques,
            )
        else:
            print('Você atingiu o limite de saques diários.')

    if opcao == 'e':
        print('==== Extrato ====')
        for i in extrato:
            print(i)
        print(f'Saldo atual: R${saldo}')

    if opcao == 'u':
        cpf = int(input("CPF: "))
        if verificarCPF(usuarios, cpf):
            nome = str(input('Nome: '))
            data_nascimento = str(input("Data Nascimento: "))
            endereco = str(input("Endereço: "))
            usuarios = criarUsuario({'cpf':cpf, 'nome':nome, 'data_nasc':data_nascimento, 'endereco':endereco, 'contas': []}, usuarios)
        else:
            print('Já existe um usuário com esse CPF.')
        
    if opcao == 'l':
        if len(usuarios) < 1:
            print('Ainda não há usuários registrados.')
        else:
            for p in usuarios:
                print('-'*10)
                print(f' CPF: {p['cpf']} \n Nome: {p['nome']} \n Data de Nascimento: {p['data_nasc']} \n Endereço: {p['endereco']} \n Contas: {p['contas']}')
                print('-'*10)

    if opcao == 'c':
        cpf = int(input("CPF para vincular a conta: "))
        if verificarCPF(usuarios, cpf):
            print('Não há nenhum usuário cadastrado com esse CPF.')
        else:
            usuarios, contas_correntes = criarConta(AGENCIA, contas_correntes, cpf, usuarios)

    if opcao == 'q':
        break