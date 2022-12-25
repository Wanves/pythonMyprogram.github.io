# import math
# from xmlrpc.client import boolean


# entero = 23 
# decimal = 31.78
# complejo = 12 + 5j
# boolean = True

# print(entero)
# print(decimal)
# print(complejo)
# print(boolean)

# resultado = entero - entero
# print(f'''
#       suma = {entero + decimal}
#       resta = {entero - decimal}
#       multiplicación = {entero * entero}
#       división = {entero / 2}
#       resto = {entero % 2}
#       potencia= {entero **3}
#       raizCuadrada = {math.sqrt(entero)}
#       ''')

num1 = int(input('Ingresa el primer número-> '))
num2 = int(input('Ingresa el segundo número-> '))

def sumar():
      return num1 + num2
print(sumar())