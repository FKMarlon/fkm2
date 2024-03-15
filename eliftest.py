MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior idade, pode tirar a CNH.")

    if idade < MAIOR_IDADE: 
        print("Ainda não pode tirar a CNH.")
