v = float(input('Informe a velocidade do veículo: '))
if v > 80:
    print('Acima da velociade permitida')
    multa = (v - 80) * 7
    print('Você foi multado em R${:.2f}'.format(multa))
else:
    print('Você está dentro da velocidade permitida')


