print('Verificar se as retas formam um triângulo')
l1 = float(input('Informe o primeiro lado: '))
l2 = float(input('Informe o segundo lado:' ))
l3 = float(input('Infrome o terceiro lado: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('Os lados formam um triângulo!')
else:
    print('Os lados NÃO formam um triângulo!')

