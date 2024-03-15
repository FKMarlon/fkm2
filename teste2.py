def sacar(valor):
    saldo = 500
    
    if saldo >= valor: 
        saldo = saldo - valor 
        print ("valor sacado!")
    print("saldo atual: ", saldo)
    
x = int (input("cm de pinto?: "))
sacar(x)

def depositar(valor):
    saldo = 500
    saldo += valor


sacar(1000)