menu ="""""
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=> """
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
while True:
    opcao = int(input(menu))
    if opcao == 1:
        valor_deposito = float(input("Valor do deposito: "))
        if valor_deposito > 0 :
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}"
            print(f"Valor de R${valor_deposito:.2f} feito com sucesso!")
        else:
            print("Operaçao falhou o valor informado e invalido")


    elif opcao == 2:
        valor_saque = float(input("Valor do saque: "))
        
        excedeu_saldo = valor_saque > saldo

        excedeu_limite = valor_saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}"
            numero_saques += 1
            print(f"Valor de R${valor_saque:.2f} feito com sucesso!")

        else:
            print(f"Operaçao falhou valor de R${valor_saque} e invalido")

    elif opcao == 3:
        print("-=-"*10)
        print("EXTRATO".center(30))
        print("-=-"*10)
        if not extrato:
            print("Nao foram realizado movimentaçao")
        else:
            extrato
        print(f"saldo: R${saldo:.2f}")


    elif opcao == 4:
        break
    else:
        print("Operaçao invalida, por favor selecione novamente a operaçao desejada.")
