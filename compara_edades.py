# Reto
# debe comparar edades de dos usuarios, y verificar quien es mayor
# debe preguntar el nombre de los usuarios
# debe mostrar el nombre del usuario mayor

nombre_1 = input('favor ingresar nombre de usuario: ')
edad_1 = int(input(f'favor ingresar edad de {nombre_1}: '))
nombre_2 = input('favor ingresar nombre de usuario a comparar: ')
edad_2 = int(input(f'favor ingresar edad de {nombre_2}: '))

if edad_1 > edad_2:
    print(f'{nombre_1} es mayor que {nombre_2}')
elif edad_1 < edad_2:
    print(f'{nombre_2} es mayor que {nombre_1}')
else:    
    print(f'{nombre_2} y {nombre_1}, tienen las mismas edades')
    