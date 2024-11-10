v = int(input('Qual a distância da viagem em Km? '))
if v > 200:
    print('O valor da viagem será de R${:.2f}'.format(v * 0.45))
else:
    print('O valor da viagem será de  R${:.2f}'.format(v * 0.5))


