saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(''' 
          ========== BANCO ============
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
''')
    opcao = input('=> ')

    if opcao == 'd':
        valor = float(input('Quanto deseja depositar? '))
        if valor > 0:
            saldo += valor
            extrato.append(f'Depositado R${valor}')
            print('Deposito feito com sucesso.')
        else:
            print('Valor inválido.')
    if opcao == 's':
        if numero_saques < LIMITE_SAQUES:
            valor = float(input('Quanto deseja sacar? '))
            if valor > limite:
                print('Você não pode sacar mais que R$500.')
            elif valor > saldo:
                print('Saldo insuficiente.')
            else:
                saldo -= valor
                extrato.append(f'Saque de R${valor}')
                
                print('Saque feito com sucesso.')
                numero_saques += 1
        else:
            print('Você atingiu o limite de saques diários.')
    if opcao == 'e':
        print('==== Extrato ====')
        for i in extrato:
            print(i)
        print(f'Saldo atual: R${saldo}')
    if opcao == 'q':
        break