animal = " cHanchItO feLiZ "
print(animal.upper())  # mayuscula
print(animal.lower())  # minuscula
# contatenacion de metodos corta espacio/primera letra en mayuscula
print(animal.strip().capitalize())
print(animal.title())  # Coloca las primeras en mayuscula
print(animal.strip())  # corta espacios
print(animal.lstrip())  # rueda a la izquierda
print(animal.rstrip())  # rueda a la izquierda
print(animal.find("tO"))  # encuentra
print(animal.replace("tO", "Ñangas"))  # rempplaza recibiendo dos argumentos
print("Ñangas" in animal)  # devuelve boleano que indica si existe el argumento
# devuelve boleano que indica si NO existe el argumento
print("Ñangas" not in animal)
