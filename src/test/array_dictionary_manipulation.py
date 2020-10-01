# Imprimir Hola Mundo

Var = 'Mundo'
Var2 = 'Mar'
print(f'Hola {Var}')

# Arrays

array = ['Argentina', 'Mexico', 'Chile', 'Perú']
array.append('Bolivia') # Añadir un valor al array
# print(array)
i = 0
for pais in array:
    print(pais)
    if pais == 'Mexico':
        print(f'El pais {pais} es parte del {Var}')
        # break  # Rompe el loop
        continue  # Sigue el loop
    if pais == 'Chile':
        array[i] = 'CCCCCChile'
        print(array[i])
    if pais == 'Perú':
        print(f'{pais} no tiene {Var2}')
        break
    i++1

# Diccionarios

diccionario = {
    'nombre': 'Matías',
    'edad': 27,
    'cursos': ['Python', 'Javascript', 'C#']
}
nombre = diccionario['nombre']

print(f'Hola {nombre}!')

diccionario['nombre'] = 'Matias Galvez'
nombre = diccionario['nombre']

print(f'Hola {nombre}!')
print(diccionario)







