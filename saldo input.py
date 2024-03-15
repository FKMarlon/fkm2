saldo = 500.0

def sacar(valor, saldo):

    if saldo >= valor:
        print("Valor sacado com sucesso!\n------------------------")
        print("retire o seu dinheiro na boca do caixa")
        saldo -= valor 
        print("Saldo atual: ", saldo)
    
    elif saldo <= valor:
        print("Você não tem dinheiro amigão")

    print("obrigado por ser nosso cliente!")
    return saldo
    

def depositar(valor, saldo):

    saldo += valor 

    print("Seu saldo atual é: " ,saldo )

print("==============================")
opcao = int(input("| [1] Sacar: [2] Depositar: |\n==============================\n Informe uma opção:"))


if opcao == 1:
    valor = float(input("Informe o valor do saque: "))
    sacar(valor, saldo)

elif opcao == 2:
    valor = float(input("Informe o valor do Depósito: "))
    depositar(valor, saldo)