N = int(input())
for _ in range(N):
    T = int(input())
    diferença = 2015-T
    if diferença>0:
        A = diferença
        sigla = 'D.C.'
    else:
        A = abs(diferença)+1
        sigla = 'A.C'
    print(f'{A} {sigla}')