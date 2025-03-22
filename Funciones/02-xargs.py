#xargs sirve para pasar argumentos a un comando

def suma(*numeros):#aqui se define la funcion y se le pasan los argumentos
    """Esta funcion suma todos los numeros que le pasemos como argumento"""
    resultado = 0#
    for numero in numeros:#aqui se le pasan los argumentos a la funcion
        resultado += numero #Aqui se hace la suma de los argumentos
        print(f"El resultado es: {resultado}")#aqui se imprime el resultado de la suma

suma(1,2,3,4)
suma(1,2)

def persona(*persona):

    resultado = ""
    for persona in persona:
        resultado += persona
        print(f"El resultado es: {resultado}")
persona("Pierre","grandett","grandett","grandett","grandett")
persona("Juan")
persona("Maria")
print("Adios")