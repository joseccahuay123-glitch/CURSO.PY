## una ferreteria tiene separada en dos listas los siguentes productos
"""
1. lista de productos de limpieza (10 productos) 
lista de materiales de costruccion (10 productos)
-----------------------------------------------------------
El dueño desea reañizar las siguientes acciones:
1. en su lista de produccion de limpieza existe un material de costruccion, debes de eliminarlos y pasar el producto ala lista que corresponde .
2. indicar si en la lista de M.C existe cemento.
3. en la lista de L.P buscar el producto lejia y cambiar su valor por lejia sapolio.
4. mostrar un mensaje doonde se detalle cual es la lista de M.C y la lista de P.L formateado.
"""
lista1:list[str]=['ace','javon','poet','lejia','antisarro','cemento','ayudin','escoba','shampu','jabonsillo']
print(lista1)

lista2:list[str]=['ladrillo','concreto','arena gruesa','arena fina','piedra chancada','yeso','alambre','carretilla','regla']
print(lista2)
--1
elemento_retirado=lista1.pop(lista1.index("cemento"))
lista2.append(elemento_retirado)

--2
buscar:int=lista2.index("cemento")
print(lista2[buscar])

--3
existe:bool="lejia" in lista1
print(existe)
print(f"si existe 'lejia' en mi lista de productos de limpieza: {lista1}")
lista1.remove('lejia')
print(lista1)
lista1.insert(3,'lejia sapolio')
print(lista1)

--4
print(f"la 'lista1' es la lista de productos de limpieza: {lista1}")
print(f"la 'lista2' es la lista de materiales de costruccion: {lista2}")

# 4 mostrar mensaje.
mensaje:str=f"""
    mi lista de productos de limpieza despues de las modificaciones queda de la siguiente manera:
    {lista1}
    -------------------------------------------------------------------------------------------
     mi lista de materiales de costruccion despues de las modificaciones queda de la siguiente manera:
     """
print(mensaje)
