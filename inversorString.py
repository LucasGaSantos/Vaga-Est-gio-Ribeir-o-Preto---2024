# Inversor de string #
print('Inversor de String')
fra = str(input('Digite uma frase: ')).strip().upper()
inv_fra = fra.split()
jun = ''.join(inv_fra)
inv = ''
for letra in range(len(jun) -1, -1 ,-1):
    inv += jun[letra]
print('O inverso de {} é {}'.format(jun,inv))
