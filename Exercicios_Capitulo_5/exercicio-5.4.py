
'''
Pedir ao usuario um número
E mostrar todos os números Impares
'''

fim = int(input('Digite o último número a imprimir: '))

x = 0

while x <= fim:
    if x % 2 == 1:
        print(x)
    x = x + 1