import time
start_time = time.time()
objetivo = int(input('Escoge un numero :'))
start_time = time.time()
epsilon = 0.01
paso = epsilon**2
respuesta=0.0

# abs = valor absoluto
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    #print(abs(respuesta**2-objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')
else:
    print(f'la raiz cuadrada del objetivo es {respuesta}')  
#tiempo ejecucion : 0.02500152587890625 segundos
#tiempo ejecucion : 134.61969995498657 segundos    
print("--- %s segundos ---" % (time.time() - start_time))    

