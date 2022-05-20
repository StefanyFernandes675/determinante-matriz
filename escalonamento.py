matriz = []
matriz_conta_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
matriz_conta_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
matriz_conta_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
matriz_conta_4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for linha in range(0, 4):
    for coluna in range(0, 5):
        numero = float(input(f"Digite o número que está na coluna {coluna+1} e linha {linha+1}: ")) 
        matriz.append(numero)

print("\n-----Matriz digitada-----")
print(f"""{matriz[0]}\t{matriz[1]}\t{matriz[2]}\t{matriz[3]}\t{matriz[4]}
          \n{matriz[5]}\t{matriz[6]}\t{matriz[7]}\t{matriz[8]}\t{matriz[9]}
          \n{matriz[10]}\t{matriz[11]}\t{matriz[12]}\t{matriz[13]}\t{matriz[14]}
          \n{matriz[15]}\t{matriz[16]}\t{matriz[17]}\t{matriz[18]}\t{matriz[19]}""")

# primeira conta

for i in range(0, 5): #primeira linha
    matriz_conta_1[i] = matriz[i]/matriz[0]

for i in range(5,16,5): #primeira coluna
    matriz_conta_1[i] = matriz[i]-matriz[i]*matriz_conta_1[0]

for i in range(6,20): #segunda, terceira e quarta linha
    if i >= 6 and i < 10:
        matriz_conta_1[i] = matriz[i]-matriz[5]*matriz_conta_1[i-5]
    elif i >= 11 and i < 15:
        matriz_conta_1[i] = matriz[i]-matriz[10]*matriz_conta_1[i-10]
    elif i>= 16 and i < 20:
        matriz_conta_1[i] = matriz[i]-matriz[15]*matriz_conta_1[i-15]   

# segunda conta 

for i in range(5,10): #segunda linha
    matriz_conta_2[i] = matriz_conta_1[i]/matriz_conta_1[6]

#primeira coluna
matriz_conta_2[0] = matriz_conta_1[0]-matriz_conta_1[1]*matriz_conta_2[5]
matriz_conta_2[10] = matriz_conta_1[10]-matriz_conta_1[11]*matriz_conta_2[5]
matriz_conta_2[15] = matriz_conta_1[15]-matriz_conta_1[16]*matriz_conta_2[5]

for i in range(1,20): #primeira, terceira e quarta linha
    if i >= 1 and i < 5:
        matriz_conta_2[i] = matriz_conta_1[i]-matriz_conta_1[1]*matriz_conta_2[i+5]
    elif i >= 11 and i < 15:
        matriz_conta_2[i] = matriz_conta_1[i]-matriz_conta_1[11]*matriz_conta_2[i-5]
    elif i >= 16 and i < 20:
        matriz_conta_2[i] = matriz_conta_1[i]-matriz_conta_1[16]*matriz_conta_2[i-10]

# terceira conta 

for i in range(10,15): #terceira linha
    matriz_conta_3[i] = matriz_conta_2[i]/matriz_conta_2[12]

#primeira coluna
matriz_conta_3[0] = matriz_conta_2[0]-matriz_conta_2[2]*matriz_conta_3[10]
matriz_conta_3[5] = matriz_conta_2[5]-matriz_conta_2[12]*matriz_conta_3[10]
matriz_conta_3[15] = matriz_conta_2[15]-matriz_conta_2[17]*matriz_conta_3[10]

for i in range(1,20): #primeira, segunda e quarta linha
    if i >= 1 and i < 5:
        matriz_conta_3[i] = matriz_conta_2[i]-matriz_conta_2[2]*matriz_conta_3[i+10]
    elif i >= 6 and i < 10:
        matriz_conta_3[i] = matriz_conta_2[i]-matriz_conta_2[7]*matriz_conta_3[i+5]
    elif i >= 16 and i < 20:
        matriz_conta_3[i] = matriz_conta_2[i]-matriz_conta_2[17]*matriz_conta_3[i-5]

# quarta conta 

for i in range(15,20): #quarta linha
    matriz_conta_4[i] = matriz_conta_3[i]/matriz_conta_3[18]

#primeira coluna
matriz_conta_4[0] = matriz_conta_3[0]-matriz_conta_3[3]*matriz_conta_4[15]
matriz_conta_4[5] = matriz_conta_3[5]-matriz_conta_3[13]*matriz_conta_4[15]
matriz_conta_4[10] = matriz_conta_3[10]-matriz_conta_3[18]*matriz_conta_4[15]

for i in range(1,15): #primeira, segunda e terceira linha
    if i >= 1 and i < 5:
        matriz_conta_4[i] = matriz_conta_3[i]-matriz_conta_3[3]*matriz_conta_4[i+15]
    elif i >= 6 and i < 10:
        matriz_conta_4[i] = matriz_conta_3[i]-matriz_conta_3[8]*matriz_conta_4[i+10]
    elif i >= 11 and i < 15:
        matriz_conta_4[i] = matriz_conta_3[i]-matriz_conta_3[13]*matriz_conta_4[i+5]

print("\n-----Matriz escalonada-----")
print(f"""{matriz_conta_4[0]}\t{matriz_conta_4[1]}\t{matriz_conta_4[2]}\t{matriz_conta_4[3]}\t{round(matriz_conta_4[4])}
          \n{matriz_conta_4[5]}\t{matriz_conta_4[6]}\t{matriz_conta_4[7]}\t{matriz_conta_4[8]}\t{round(matriz_conta_4[9])}
          \n{matriz_conta_4[10]}\t{matriz_conta_4[11]}\t{matriz_conta_4[12]}\t{matriz_conta_4[13]}\t{round(matriz_conta_4[14])}
          \n{matriz_conta_4[15]}\t{matriz_conta_4[16]}\t{matriz_conta_4[17]}\t{matriz_conta_4[18]}\t{round(matriz_conta_4[19])}""")  

print(f"\nx = {round(matriz_conta_4[4])}\ny = {round(matriz_conta_4[9])}\nz = {round(matriz_conta_4[14])}\nw = {round(matriz_conta_4[19])}")