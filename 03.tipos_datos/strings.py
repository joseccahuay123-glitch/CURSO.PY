#Este tipo de dato sirve para almaxenar informacion de tipo texto, texto simple o extenso.
# para alm,acenar un dato de tipo texto l informacion deve de estar encerrada entre comillas ("",'',"""").
## _ comillas dobles ("").
## - comillas simples('').
## - docstrng ("""").
nombre_instituto:str="ISTP-JMA"
nombre_curso:str='lenguaje de progamacion'
descripcion_curso:str="""
el curso de "lenguajes de programacion",
tiene una duracion de swemestre 
educativo con 6 horas semanales y
aprender a programar en el lenguaje 
"python"
 """

## los string tienen funciones basicas para poder interactuar con los datos que estamos almacenando 
## la estroctura de una funcion es la siguiente
## nombre_funcion(argumento)
## *argumento - Es un valor que se le pasa a un funcion, funcion que en base a su programacion retornara otro valor distinto al pasado por el argumento
print("hola mundo") # salida: hola mundo
print("hola, mundo") # salida: hla mundo

# funcion para mostrar la cantidad de caracteres que tiene un string -texto
texto: str = "hola mundo"
cantidad_caracteres:int= len(texto)
print("cantidad de caracteres:",cantidad_caracteres)

#forma de acceder a un caracter especial 
## para esto tenemos que entender que pythooooooooon asigna a cada caracteres con un indice de base cero

#ejemplo: celia 
# indices 01234
nombre_celia:str = "celia"
print (nombre_celia)
print(nombre_celia[2])

#troceado de texto
## para esto se utiliza la notacion de corchetes con la diferencia quese debe indicar un indice inicial y un indice final del texto a extraer.
##texto [i_inicial:i_final]
vocales:str ="aeiou"
print(vocales[1:3])
