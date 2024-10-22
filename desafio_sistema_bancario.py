menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
qtde_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!!!")

        else:
            print("Depósito não realizado! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        ultrapassou_saldo = valor > saldo

        ultrapassou_limite = valor > limite

        ultrapassou_saque = qtde_saques >= LIMITE_SAQUES

        if ultrapassou_saldo:
            print("Não foi possível concluir! Seu saldo é insuficiente.")

        elif ultrapassou_limite:
            print("Não foi possível concluir! O valor informado ultrapassa o limite, que é de R$ 500,00 por saque.")

        elif ultrapassou_saque:
            print("Não foi possível concluir! Você ultrapassou a quantidade, que são 3, de saques diário.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            qtde_saques += 1
            print("Saque realizado! Retire o dinheiro.")

        else:
            print("Saque não realizado! Informe um valor válido.")

    elif opcao == "3":
        print(" EXTRATO ".center(50, "■"))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(" Obrigado por usar nossos serviços! ".center(50,"■"))

    elif opcao == "0":
        break

    else:
        print("Você selecionou uma opção inválida, favor selecionar umas das opções disponíveis.")