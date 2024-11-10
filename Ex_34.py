sal = float(input('Informe o salário: R$ '))
if sal > 1250:
    pcem = 0.10 * sal
    print('O seu salário atual é de R${:.2f} e terá um aumento de R${:.2f} totalizando R${:.2f} '.format(sal, pcem, pcem + sal ))
else:
    pcem = 0.15 * sal
    print('O seu salário atual é de R${:.2f} e terá um aumento de R${:.2f} totalizando R${:.2f}'.format(sal, pcem, pcem + sal))
