N = int(input()) #número de estrelas
Estrelas = [int(x) for x in input().split()]
estrelas_atacadas = 0
posição = 0

while posição in range(N): #repete enquanto a posição estiver correspondendo à um elemento da lista Estrelas
    estrelas_atacadas += 1
    i = posição #posição referente à estrela
    C = Estrelas[i] #número de carneiros da estrela
    if C == 0:
        posição -=1 
    else:
        if C%2==0:
            Estrelas[i]-=1
            posição -= 1
        else:
            Estrelas[i]-=1
            posição += 1

carneiros_não_roubados = sum(Estrelas)
print(estrelas_atacadas,carneiros_não_roubados)