print('--Cursos--')
print('Matematica', 'Biología', 'Lenguaje', 'Ciencias')
curso = input('Ingrese el curso elegido-> ')
if curso in ('Matematica', 'Biología', 'Lenguaje', 'Ciencias'):
    print(f'Curso {curso} es seleccionado')
else:
    print('No existe ese curso..')