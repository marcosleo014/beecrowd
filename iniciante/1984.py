n = input()
número = list(n)
número_invertido = []
while len(número)!=0:
    dígito = número.pop(-1)
    número_invertido.append(dígito)
print(''.join(número_invertido))