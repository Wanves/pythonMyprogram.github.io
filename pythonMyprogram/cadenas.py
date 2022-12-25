texto = 'Hacemos de algo siple algo extraordinario'

print(texto.lower())
print(texto.upper())
print(texto.strip())
print(texto.title())

print(texto.find('algo'))
print(texto.count('a'))

textoFinal = texto.replace('algo', '*')
print(textoFinal)

valor = texto.isnumeric() 
print(valor)

cadenaSeparada = texto.split(' ')
print(cadenaSeparada)