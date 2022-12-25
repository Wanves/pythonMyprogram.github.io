texto1 = 'Hola Mundo '
texto2 = 'Genial '

print(f'''
      {texto1 + texto2}
      {texto1}
      ''')

saludando = 'Saludo: {}{}'.format(texto1, texto2)
print(saludando)

saludando2 = '{x}Saludo: {y}{x}'.format(x=texto1,y=texto2)
print(saludando2)

