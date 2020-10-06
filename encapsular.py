def busqueda_exaustiva():
    objetivo = int(input('Escoge un entero:'))
    respuesta = 0

    while respuesta **2 < objetivo:
        respuesta +=1

    if respuesta**2==objetivo:    
        return print(f'la raiz cuadrada de {objetivo} es {respuesta}')
    else:
        return print(f'{objetivo} no tiene raiz cuadrada exacta')

def busqueda_aproximacion():
    objetivo = int(input('Escoge un numero :'))
    epsilon = 0.01
    paso = epsilon**2
    respuesta=0.0

    # abs = valor absoluto
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        #print(abs(respuesta**2-objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        return f'No se encontro la raiz cuadrada {objetivo}'
    else:
        return f'la raiz cuadrada del objetivo es {respuesta}'  

def busqueda_binaria():
    objetivo = int(input('Escoge un numero :'))
    epsilon = 0.1
    bajo= 0.0
    # si nuestro objetivo es menor a 1.0 vamos a empezar desde 1.0
    alto= max(1.0, objetivo) 
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo ) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2

    #print statement
    return f'la raiz cuadrada de {objetivo} es {respuesta}'

print(f'')
print(f' ------------------ Seleccione Tipo de busqueda -----------------------')
print(f' ----------------------------------------------------------------------')
print(f' (1) Busqueda_exaustiva')
print(f' (2) Busqueda_aproximacion')
print(f' (3) Busqueda_binaria')
print(f' ----------------------------------------------------------------------')
opcion = int(input('Ingrese el número de su opcion: '))
resultado=""
if opcion == 1:
    print(f' (1) Busqueda_exaustiva')
    resultado = busqueda_exaustiva()
elif opcion == 2: 
    print(f' (2) Busqueda_aproximacion')
    resultado = busqueda_aproximacion()
else:
    print(f' (3) Busqueda_binaria')
    resultado = busqueda_binaria()

print(resultado)
