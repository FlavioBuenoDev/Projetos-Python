
'''
def generator(n=0):
    yield 1  # Pausar
    print('Continuando ...')
    yield 2  # Pausar
    print('Mais uma vez...')
    yield 3  # Pausar
    print('Vou terminar')
    return 'Acabou'


gen = generator(n=0)
for n in gen:
    print(n)
'''


def generator(n=0, maximum=10):
    while True:
        # yield - pausa
        yield n
        n += 1

        if n > maximum:
            return


gen = generator(maximum=1000)
for n in gen:
    print(n)
