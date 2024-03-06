# SEQUÊNCIA DE FIBONACCI #
from time import sleep 
print('Sequência de Fibonacci')
sleep(1)
print('Para isso, preciso que você escolha um número')
sleep(1)
n = int(input('Escolha o número: '))
fibbonacci = int(input('Quantos números de Fibbonacci você quer? '))
c = 1
t1 = 0
t2 = 1
print('{} -> {}'.format(t1,t2),end=' ')
cont = 3
t3 = 0
nFib = False
while cont <= fibbonacci:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print('-> {}'.format(t3),end= ' ')
    cont += 1
    if t3 == n:
        nFib = True

if nFib or n == 0:
    print('')
    print('O número inserido pertence a Fibbonacci')
else:
    print('')
    print('O número inserido não pertence a sequência')
