tamanho_matriz = 0
matriz = []

print("-----Calculador de determinante de matriz até matriz 3X3-----")
while tamanho_matriz > 3 or tamanho_matriz <= 0:
    tamanho_matriz = int(input("\nQuantas colunas e linhas tem a matriz. \nExemplo (3X3): 3 \n Digite: "))
print(f"Matriz {tamanho_matriz}X{tamanho_matriz}")

for linha in range(0, tamanho_matriz):
    for coluna in range(0, tamanho_matriz):
        numero = float(input(f"Digite o número que está na coluna {coluna+1} e linha {linha+1}: ")) 
        matriz.append(numero)

print("\n-----Matriz digitada-----")
if tamanho_matriz == 1:
    print(f"{matriz[0]}")
    determinante = matriz[0]
elif tamanho_matriz == 2:
    print(f"{matriz[0]}\t{matriz[1]}\n{matriz[2]}\t{matriz[3]}")
    determinante = matriz[0] * matriz[3] - matriz[1] * matriz[2]
else:
    print(f"{matriz[0]}\t{matriz[1]}\t{matriz[2]}\n{matriz[3]}\t{matriz[4]}\t{matriz[5]}\n{matriz[6]}\t{matriz[7]}\t{matriz[8]}")
    #sarrus
    determinante = matriz[0] * matriz[4] * matriz[8] + matriz[1] * matriz[5] * matriz[6] + matriz[2] * matriz[3] * matriz[7] - matriz[1] * matriz[3] * matriz[8] - matriz[0] * matriz[5] * matriz[7] - matriz[2] * matriz[4] * matriz[6]
print(f"\nDeterminante = {determinante}")