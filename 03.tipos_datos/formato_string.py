#utlizar tecnicas para unir string en uno solo
## concatenacion
#cuando este operador se encuentra entgre dos textos se convierte en el operador de cancatenacion  cuando esta entre dos numeros es el operador de adicion (suma)
nombre:str = "noemi"
apellido:str = "noseprofesor"
nombre_completo:str = nombre+" "+apellido
print(nombre_completo) #salida: noemi noseprofesor

##opcion mas optima de concatenacion
print(nombre,apellido)
# f-string (tarea)
# formato de string esto sirve para formatear string con variables de python y para sus se requiere de una f antesde escribir un string, si se desea escribir codigo python en el string se debe encerrar entre llaves {}
nombre:str = "gianfranca"
edad:int =14
#mensaje de salida me diga mi nombre es {} y teengo edad 
print(f"mi nombre es {nombre}y tengo {edad}")

##PLANTILLAS DE STRING
nombre_cliente:str=input("ingrese tu nombre: ")
ruc_cliente:int=int("ingrese ruc: ")
direccion_cliente:str=input("digite direccion: ")
codigo_producto:str=input("ingrse codigo producto: ")
nombre_producto:str=input("ingrse nombre del producto: ")
precio_unidad:float=float(input("ingrese el precio del producto: "))
cantidad_producto:float=float(input("cantidad a comprar"))
precio_total: float= precio_unidad * cantidad_producto

plantilla:str=f
cliente: {nombre_cliente}.........RUC:  {ruc_cliente}
direccion: {direccion_cliente}