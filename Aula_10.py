#nome = str(input('Qual o seu nome? ')).strip().title()
#print('Prazer em conhecê-lo, {}'.format(nome))
#if nome == 'Sandro':
  #  print('Você tem um belo nome!')
#else:
 #   print('Seu nome é comum')
#print('Bom dia!')
import math
from math import trunc
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Média: {}'.format(trunc(media)))
#if media >= 6:
#    print("PARABÉNS")
#else:
#    print('ESTUDE MAIS')
print('PARABÉNS' if media>= 6 else 'ESTUDE MAIS')


