import random
n = int(input('Informe um número entre 0 a 5: '))
n_aleatorio = random.randint(0,5)
print('Numero sorteado: {}'.format(n_aleatorio))
if n == n_aleatorio:
    print('Parabéns! você escolheu {} e acertou.'.format(n))
else:
    print('Você escolheu {} e Infelizmente errou.'.format(n))








