saludo = "Hola global" # Variable global
#EL alcance de las funciones
def saludar():
    saludo = "Hola mundo"
    

def otro_saludo():
    saludo = "Hola universo" 
    print(saludo) # Hola

saludar() # Hola
print(saludo) # Hola global



