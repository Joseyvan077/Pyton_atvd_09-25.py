# Inicialize um dicionário para rastrear as contagens
contagens = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

# Solicite ao usuário a nota de satisfação e atualize as contagens
total_clientes = int(input("Quantos clientes avaliaram a empresa? "))
for _ in range(total_clientes):
    nota = int(input("Informe a nota de satisfação (de 1 a 5): "))
    if nota >= 1 and nota <= 5:
        contagens[nota] += 1
    else:
        print("Nota inválida. Por favor, insira uma nota de 1 a 5.")

# Imprima o número de clientes que avaliaram com cada nota
for nota, quantidade in contagens.items():
    print(f"Nota {nota}: {quantidade} clientes")