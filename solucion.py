
# Fuente Discreta sin Memoria (Discrete Memoryless Source,DMS)

from random import choices

def fuente(tabla: dict): 
    simbolos = list(tabla.keys())
    frecs = list(tabla.values())

    def f(cantidad):
        return ''.join(choices(simbolos, weights=frecs, k=cantidad))
    return f

# Análisis de frecuencias 


# Arbol de Huffman

# Tabla de códigos

# Codificación y Decodificación
