n1 = input("Ingresa el primer numero:  ")
n2 = input("Ingresa el primer segundo:  ")

n1 = int(n1)
n2 = int(n2)
suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
divi = n1 / n2

mensaje = f"""(Para los numeros {n1} y {n2}),
el resultado de la suma  es {suma}.
el resultado de la resta  es {resta}.
el resultado de la multiplicacion  es {multi}.
el resultado de la division  es {divi}.
"""

print(mensaje)
