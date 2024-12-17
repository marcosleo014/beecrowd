while True:
    try:
        horário = [int(x) for x in input().split(':')]
        tempo = horário[0]*60+horário[1] + 60
        X = tempo - 480
        if X>0:
            print(f'Atraso maximo: {X}')
        else:
            print('Atraso maximo: 0')
    except EOFError:
        break