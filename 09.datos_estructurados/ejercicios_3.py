Alumnos:list[str]=['deduardo','noemi','emerson','yo']
print(Alumnos)
# eliminarpor valor.
Alumnos.remove('yo')
print(Alumnos)
# Eliminar el ultimo valor por valor.
Alumnos.pop()
print(Alumnos)
## pop tambien elimina elementos por indice.
Alumnos.pop(1)
print(f"mi lista de desaprovados sera: {Alumnos}")
### el metodo pop tiene la caracteristicas de recuperar el elemento eliminado eso quiere decir que podemos almacenarlo en la variable.
print(f"elimine: {'a'}")

## tengo una lisdta de marcas de vehiculos(toyota,nissan,datsun,daewod,simo mack,nazda,onda) crear un programa que realice lom siguiente:
"""
1. eliminar el 5 elemento.
2. en su lugar agregar la marca mitsubishi
3. buscar nissan y mostrar su valor por terminal
4. mostrar si existe honda en mi lista de vehiculos
"""
vehiculos:list[str]=('toyota','nissan','datsun','daewod','simo mack','nazda','honda')
print (vehiculos)

vehiculos.remove('simo mack')
print(vehiculos)

vehiculos.insert(4,'mitsubishi')
print(vehiculos)

buscar:int=vehiculos.index("nissan")
print(vehiculos[buscar])


existe:bool="honda" in vehiculos
print(f"existe honda en mi lista de3 vehiculos: {vehiculos}")






