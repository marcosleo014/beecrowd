n = int(input())
alunos = []
for _ in range(n):
    aluno = [float(x) for x in input().split()]
    alunos.append(aluno)
alunos.sort(key= lambda k: k[1])
if alunos[n-1][1]<8:
    print('Minimum note not reached')
else:
    print(int(alunos[n-1][0]))
