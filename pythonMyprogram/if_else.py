edad = int(input('Ingresa tu edad--> '))
     
if edad >= 18 and edad >=0:
    print('Eres mayor de edad')
    print('Edad correcta') 
elif edad < 0:
    print('Error--edad negativa, otra oportunidad')
    while edad < 0:
        edad = int(input('Ingresa tu edad--> '))
        if edad >= 18 and edad >=0:
            print('Eres mayor de edad')
            print('Edad correcta')
        else :
            print('Eres menor de edad')      
else :
    print('Eres menor de edad')
    
