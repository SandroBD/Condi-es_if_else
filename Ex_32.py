from datetime import date
print('---FERIFICADOR DE ANOS BISSEXTO')
ano = int(input('Informe o ano: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0) and ( ano % 100 != 0 or ano % 400 == 0):
    print('O ano de {} é uma ano bissexto!'.format(ano))
else:
    print('O ano de {} NÃO é um ano bissexto!'.format(ano))
print('---FIM DO PROGRAMA---')


