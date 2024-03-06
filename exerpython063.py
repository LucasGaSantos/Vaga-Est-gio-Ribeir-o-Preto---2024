# SEQUÊNCIA DE FIBONACCI #
from time import sleep 
print('Sequência de Fibonacci')
sleep(1)
print('Para isso, preciso que você escolha um número')
sleep(1)
print('Com esse número, irei mostrar até aonde vai a sequência')
n = int(input('Escolha o número: '))
c = 1
t1 = 0
t2 = 1
print('{} -> {}'.format(t1,t2),end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print('-> {}'.format(t3),end= ' ')
    cont += 1
print('FIM')