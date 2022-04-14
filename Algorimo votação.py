C1 = 0
C2 = 0
C3 = 0
Nulos = -1
Voto = 0
while(Voto != -1):
    Voto = int(input("Seja bem vindo ao sistema de votação !\nPara votar digite:\n'1' para votar no candidato 1\n'2' para votar no candidato 2\n'3' para votar no candidato 3\nQualquer outro número inteiro diferente de -1, 1, 2 e 3 para votar nulo\nDigite seu voto a seguir\n======================> "))
    if(Voto == 1):
        C1 = C1 + 1
    elif(Voto == 2):
        C2 = C2 + 2
    elif (Voto == 3):
        C3 = C3 +3
    else:
        Nulos = Nulos + 1
print(f"\n\n\n\n\n\n\nEleição finalizada, o resultado foi:\nO candidato 1 ficou com {C1} votos\nO candidato 2 ficou com {C2} votos\nO candidato 3 ficou com {C3} votos\nA quantidade de votos nulos foi de {Nulos} votos.")
Total = C1 + C2 + C3 + Nulos
if(C1 > C2 and C1 > C3 and C1 >= Nulos):
    P = (C1 * 100)/Total
    print(f"O candidato 1 ganhou com {C1} votos, e com uma porcentagem de {P:.2f}% do total de votos.")
elif(C2 > C3 and C2 >= Nulos):
    P = (C2 * 100)/Total
    print(f"O candidato 2 ganhou com {C2} votos, e com uma porcentagem de {P:.2f}% do total de votos.")
elif(C3 >= Nulos):
    P = (C3 * 100)/Total
    print(f"O candidato 3 ganhou com {C3} votos, e com uma porcentagem de {P:.2f}% do total de votos.")
else:
    P = (Nulos * 100)/Total
    print("Os votos nulos foram maiores que o da quantidade de votos nos outros candidatos, os nulos são {P: .2f}% dos votos, a eleição terá de ser refeita.")