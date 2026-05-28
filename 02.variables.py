# para declarar un nombre en python usaremos la convencion snake_case
## reglas
### 1. el nombre de la variable debe indicar que dato se esta almacenando
### 2, las variables no deben contener numeros ni mcaracteres especiales (@, /, !, ?).
nombre_curso="lenguaje de programacion"
creditos_curso=3
horas_semanales-curso=6
# ADVERTENCIA - LAS  variable son mutables 
print(creditos_curso) # salida: 3
creditos_curso= 10 
print(creditos_curso) # salida: 10 

# NOTA IMPORTANTE POR TODO EL CURSO - CADA VE QUE DECLAREMOS VARIABLES USAREMOS ANOTACIONES PARA INDICAR QUE TIPO DE DATO SE DEVE ALMACENAR

nombre_alumno:str = "eduardo"
edad_alumno: int = 28
estatura_alumno: float = 1.59
asistencia_alumno: bool = True
amigos_alumno: list = []
direccion_alumno: dict = {
"n_calle":"psj belen",
"numero de casa":230,
"barrio":"ccayau" 
}

# Asignacion de un variable a otra variable
edad_alumno:int=21
edad_docente:int= edad_alumno

## INPORTAR NO OLVIDAR 
###Un decorador en python nos edentifica que tipo de dato va almacenar nuestra variable 
### los decoradores que python trae por defectos son:

###### datos primitivos ######
#decoradores para datos primitivos
### :int -enteros
### :float -decimales, comaflotante
### :str -string texto
### :bool _datos voleanos true o false

###### datos estrocturados ######
#decoradores para datos estrocturados
### :list -listas
### :dic _diccionarios

## como asemos uso de la variables
## para aser uso del dato almacenado en una variable vasta con aser el llamado del nombre de la variable
primer_numero:int =30
segundo_numero:int=20
suma: int = primer_numero+segundo_numero