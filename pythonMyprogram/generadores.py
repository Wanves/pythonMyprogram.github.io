# def generaMultiplos7(limite):
#     numero = 1
#     listaNumeros = []
#     while numero <= limite:
#         listaNumeros.append(numero*7)
#         numero = numero + 1
#     return listaNumeros
# print(generaMultiplos7(5))


def generaMultiplos7(limite):
    numero = 1
    while numero <= limite:
        yield numero*7
        numero += 1
        
obtieneMultiplo7 = generaMultiplos7(5)
# # print(obtieneMultiplo7)

# for i in obtieneMultiplo7:
#     print(i)


print(next(obtieneMultiplo7))
print('a')
print(next(obtieneMultiplo7))
print('b')
print(next(obtieneMultiplo7))
print('c')