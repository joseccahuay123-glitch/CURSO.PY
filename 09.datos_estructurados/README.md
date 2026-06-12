# Datos estructurados
- tenemos 3 tipos de datos primarios(string, numerico y boleano)
- (tenemos 2 tipos de datos estructurados  (listas, diccionarios))
## listas📃
son la manera de como python puede organizar multiples tipos de datos en una sola variable.
se puede tener :
- listas de tipo numerica
- listas de tipo texto
- listas de tipo mixto
python nos permite accedera estas listas a traves de indices. los indices son ascendentes empesando del numero 0.
## creacion de listas🎃
para  listas solo hasta encerrar los elementos que deseamos almacenar con [] imediatamente despues del operador de asignacion =
```python
## Creando una lista vacía
lista:list=[]
# lista numerica
## OJÓN: Los elementos de una lista se separan por comas😮
lista_numerica=list[int]=[3,8,4]

lista_num_mixto:list[int|float]=[3.6,7,0.7]

#lista mixta
lista_mixta:list=['pedro',20,falce,1.67]
```
### Aceder y modificar elementos de una lista
para poder acceder a un elementom de una lista trabajamos con los indices que python lom asigna a cada elemento que tenemos
- los indices pocitivos(comienzan de cero y van de isquierda a derecha)
- los indices negativos(comienzan de -1 y van de derecha a izquierda)
con  estos indices podemos acceder al valor del elemento y tambien podemos modificarlos.
Tenemos dos formas de acceder al elemento:
- por indice(pocición)
- por rango(slicing)
```python
frutas :list[str]=['🍏','🍐','🍑','🍒']
# posicion o indice
# acceder al tercer elemento
print(frutas[2])
# acceder al cegundo elemto por su indice negativo
print(frutas[-3])
```

```python
# acceder por rango
Para extraer varios elementos contiguos, indica los indices por dos puntos.

print(frutas[])

# Buscar
## este metodo permite uvicar a traves del valor el primer elemento (la primera considencia) dentro de una lista, este metodo es index
amantes:list[str]=['chapo','cristian','emerson','victor']
buscar:int=amantes.index("victor")#retora un indice si exsiste 3
amantes[buscar]
## busqueda por pertenencia
existe:bool="chapo" in amantes
```

## diccionarios