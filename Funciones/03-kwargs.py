def get_product(**datos ):
    print(datos["id"], datos ["nombre"])

get_product(id="484758", 
            nombre="Iphone 14", 
            precio="precio_producto") 

#los kwargs son argumentos que se pasan a una funcion como un diccionario
   