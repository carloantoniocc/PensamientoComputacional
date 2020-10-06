objetivo = int(input('Escoge un numero :'))
epsilon = 0.1
bajo= 0.0
# si nuestro objetivo es menor a 1.0 vamos a empezar desde 1.0
alto= max(1.0, objetivo) 
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo ) >= epsilon:
    print(f'bajo: {bajo} alto: {alto} respuesta: {respuesta} respuesta**2: {respuesta**2}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    respuesta = (alto + bajo) / 2

#print statement
print(f'la raiz cuadrada de {objetivo} es {respuesta}')