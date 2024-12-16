A,B = [float(x) for x in input().split()]
fator_de_aumento = (B/A-1)*100
print(f'{fator_de_aumento:.2f}%')