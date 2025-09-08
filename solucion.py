
# Fuente Discreta sin Memoria (Discrete Memoryless Source,DMS)

from random import choices # importa funcion choices del modulo random

def fuente(tabla: dict): # definición de fcion fuente cuyo argumento es un diccionario (estructuras que almacenan pares de clave y valor) 
    simbolos = list(tabla.keys()) # crea una lista con las claves del diccionario
    frecs = list(tabla.values()) # crea una lista con los valores del diccionario

    def f(cantidad): 
        return ''.join(choices(simbolos, weights=frecs, k=cantidad)) # '' cadena vacía como separador para unir; .join() une todos los elementos de una lista en una cadena, choices funcion para elegir aleatoriamente
    return f

# Análisis de frecuencias 
def analisis(cadena): 
    frecs = {}  # crea un diccionario vacío
    for s in cadena: # recorre cadena 
        if s in frecs: 
            frecs[s]+=1 # aumenta el contador si el simbolo s ya estaba en el diccionario
        else: 
            frecs[s]=1 # si aparece s por primera vez se lo agrega al diccionario con valor 1
    return frecs

# Arbol de Huffman
def huffman(frecs):  # funcion cuyo argumento es el diccionario frecs
    arboles = [[[k],v] for k,v in frecs.items()] # convierte al diciconario en una lista de lista, cada sublista es una hoja del arbol
    arboles.sort(key=lambda x:x[1]) # ordena las hojas según su frecuencia (menor a mayor)
    # Combinar las hojas hasta quedar en la raiz del arbol es equivalente a que quede una lisa con dos elemetos donde el primer elemento será una lista anidada con todas las hojas y el segundo elemento la suma de frecuencias de todas las hojas
    while len(arboles)>1:  # mientras haya más de un nodo en la lista
        # Se extrae las 2 hojas y ó nodos con menor frecuencia, para combinarlos en un nodo 
        a=arboles.pop(0)    # extrae la primera hoja o nodo
        b=arboles.pop(0)    # extrae la segunda hoja o nodo
        y=[[a[0],b[0]],a[1]+b[1]] # crea un nuevo nodo combinandeo a y b
        arboles.append(y)   # agrega y al final de la lista arboles
        arboles.sort(key=lambda x:x[1]) # ordena los nodos según su frecuencia (menor a mayor)
    return arboles[0][0] # devuelve la lista anidada con las hojas  

# Tabla de códigos
def tabla_codigo(arbol, prefijo = ''): # la funcion a partir de una lista arbol entregará un diccionario, se inicializa con un prefijo vacío y en cada llamada recursiva se aumenta un 0 si se va a la izquierda y un 1 si se va a la derecha
    n= len(arbol) # mide la cantidad de elemtos en el nodo

    match n:
        case 2: # tiene dos ramas, se hacen llamadas recursivas
            iz=tabla_codigo(arbol[0],prefijo+'0') # se agrega 0 al prefijo para la rama izquierda
            de=tabla_codigo(arbol[1],prefijo+'1') # se agrega 1 al prefijo para la rama derecha
            return iz|de # | une dos diccionaros en uno nuevo, une los diccionarios generados en ambas ramas
        case 1: # es una hoja
            return{arbol[0]:prefijo} # devuelve un diccionario el símbolo es la clave y el prefijo su valor
        case 0: # nodo vacio
            return dict() # devuelve un diccionario vacío
        case _:
            raise ValueError("Arbol mal formado")



# Codificación y Decodificación
