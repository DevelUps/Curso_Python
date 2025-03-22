#funcion print("hola mundo") que imprime un mensaje de bienvenida

def saludo():
    print("Hola mundo!")
    print("Bienvenidos a Python")

saludo()

#------------------------------------------------------------
#Argumentos y parametros en funciones
def hola(nombre, apellido):#este es un parametro
    print("Hola mundo!")
    print(f"Bienvenid@ {nombre} {apellido}") # parametro de la funcion

hola("Pierre","grandett")#este es un argumento del parametro nombre
hola("Juan", "Perez")#este es un argumento del parametro nombre
hola("Maria", "feliz")#este es un argumento del parametro nombre

#pero todo lo anterior esta mal por que tengo dos parametros y solo estoy pasando un argumento valida

#------------------------------------------------------------
#Argumentos opcionales
def saludo(nombre, apellido="campechano"):#este es un parametro
    print("Hola mundo!")
    print(f"Bienvenid@ {nombre} {apellido}")

saludo("Pierre","grandett")
saludo("Juan")#en este caso no se pasa el argumento del parametro apellido
saludo("Maria")#en este caso no se pasa el argumento del parametro apellido

#------------------------------------------------------------
#Argumentos nombrados
def saludo(nombre, apellido="campechano"):#este es un parametro
    print("Hola mundo!")
    print(f"Bienvenid@ {nombre} {apellido}")
    saludo(apellido="grandett", nombre="Pierre")
    saludo(nombre="Juan")#en este caso no se pasa el argumento del parametro apellido
