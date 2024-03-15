def gerarletras_aleatorias():
    # Seed baseada no timestamp
    seed = 181 # Número arbitrário
    num = seed
    letras_aleatorias = ''
    for seed in range(5):
        num = (num * 1103515245 + 12345) & 0x7fffffff
        letra = chr(ord('a') + num % 26) # Convertendo para ASCII
        letras_aleatorias += letra
    return letras_aleatorias

print(gerarletras_aleatorias())