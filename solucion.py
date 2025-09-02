
# Fuente Discreta sin Memoria (Discrete Memoryless Source,DMS)

from random import choices

def fuente(tabla: dict): 
    simbolos = list(tabla.keys())
    frecs = list(tabla.values())

    def f(cantidad):
        return ''.join(choices(simbolos, weights=frecs, k=cantidad))
    return f

# Análisis de frecuencias 
def analisis(cadena): 
    frecs = {}
    for s in cadena:
        if s in frecs:
            frecs[s]+=1
        else: 
            frecs[s]=1
    return frecs

# Arbol de Huffman

# Tabla de códigos

# Codificación y Decodificación
