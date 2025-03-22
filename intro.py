import math

"""
Introducción a los Fundamentos de Python

Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. 
Es conocido por su sintaxis clara y legible, lo que lo hace ideal tanto para principiantes 
como para desarrolladores experimentados. A continuación, se presentan algunos de los 
fundamentos básicos de Python:

1. Variables y Tipos de Datos:
    - Python es un lenguaje de tipado dinámico, lo que significa que no es necesario 
      declarar el tipo de una variable antes de usarla.
    - Tipos de datos comunes incluyen: int (enteros), float (números de punto flotante), 
      str (cadenas de texto), bool (booleanos), list (listas), dict (diccionarios), 
      entre otros.

2. Estructuras de Control:
    - Python soporta estructuras de control como if, for, y while para la toma de decisiones 
      y la iteración.
    - Ejemplo:
      ```python
      if x > 0:
            print("x es positivo")
      else:
            print("x es negativo o cero")
      ```

3. Funciones:
    - Las funciones en Python se definen usando la palabra clave def.
    - Ejemplo:
      ```python
      def saludar(nombre):
            return f"Hola, {nombre}!"
      ```

4. Manejo de Errores:
    - Python utiliza bloques try-except para manejar excepciones.
    - Ejemplo:
      ```python
      try:
            resultado = 10 / 0
      except ZeroDivisionError:
            print("No se puede dividir por cero")
      ```

5. Módulos y Paquetes:
    - Python tiene una amplia biblioteca estándar y permite la creación de módulos y paquetes 
      para organizar el código.
    - Ejemplo:
      ```python
      print(math.sqrt(16))
      ```

Estos son solo algunos de los conceptos básicos de Python. A medida que avances en tu 
aprendizaje, descubrirás muchas más características y funcionalidades que hacen de Python 
un lenguaje poderoso y versátil.
"""
