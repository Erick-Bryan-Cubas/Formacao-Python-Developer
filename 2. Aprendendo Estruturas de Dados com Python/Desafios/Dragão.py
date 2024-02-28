C = int(input())  # Leitura do número de casos

for i in range(C):
    valor = int(input())  # Leitura do valor para cada caso
    
    # Condição para verificar se o valor é maior que 8000
    if valor > 8000:
        print("Mais de 8000!")  # Ajuste conforme a saída esperada
    else:
        print("Inseto!")
