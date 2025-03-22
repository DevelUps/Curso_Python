saludo = "Hola global" # Variable global
#EL alcance de las funciones
def saludar():
    global saludo 
    

def otro_saludo():
    saludo = "Hola universo" 
    print(saludo) # Hola

otro_saludo() # Hola universo
saludar() # Hola
print(saludo) # Hola global



