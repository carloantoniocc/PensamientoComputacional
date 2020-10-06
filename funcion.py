# siempre comienzan con el key def que significa definicion
def funcion(<parametros>):
    <cuerpo>
    return <expresion>

# return statement sino se define vuelve un Non: ausencia de valor

def suma(a,b):
    total = a+b
    return total

suma(2,3)

# Argumentos de keyword 
def nombre_funcion(nombre, apellido, inverso=False)
# se puede inicializar un argumento
    if inverso:
        return f'{nombre} es inverso'
    else:
        return f'{nombre}'

# para llamar se utiliza ubicacion posicional del parametro
nombre_funcion('carlos', 'cornejo')
nombre_funcion('carlos','cornejo',inverso=true)
nombre_funcion(apellido='cornejo',nombre='carlos',inverso=false)

