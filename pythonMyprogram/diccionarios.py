diccionario = {'España':'Madrid','Perú':'Lima','Argentina':'Buenos Aires'}

print(diccionario['Argentina'], diccionario['España'], diccionario['Perú'])
diccionario['Venezuela'] = 'Caracas'
print(diccionario)
diccionario['Venezuela'] = '*|*'
print(diccionario)

del diccionario['Perú']
print(diccionario)

diccionario2 = {'Smith':'Neo','30':True,'sueldo':'300000'}
print(diccionario2['30'])

llaves = ('España', 'Francia', 'Inglaterra')

dicPaises = {llaves[0]:'Madrid', llaves[1]:'Paris', llaves[2]:'Londres'}
print(dicPaises)
print(dicPaises.keys())

print(dicPaises.get('Argentina','No se encuentra'))
print(dicPaises.values())
valores = tuple(dicPaises.values())
print(valores)