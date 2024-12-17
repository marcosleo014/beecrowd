i = 1
while True:
    try:
        x = int(input())
    except EOFError:
        break
    if x==0:
        msg = 'numero'
    else:
        msg = 'numeros'
    seq = ['0']
    for N in range(1,x+1):
        for _ in range(N):
            seq.append(str(N))
    print(f'Caso {i}: {len(seq)} {msg}')
    print(' '.join(seq))
    print()
    i+=1