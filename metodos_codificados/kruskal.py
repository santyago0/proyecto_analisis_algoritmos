import networkx as nt
import matplotlib.pyplot as mt
import os

# Grafo desde un archivo .txt
def grafo_archivo(ruta_archivo):
    grafo = nt.Graph()
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Eliminar espacios en blanco
            linea = linea.strip()
            # Separar los atributos por ','
            parts = linea.split(',')
            # Guardar los atribulos en variables
            u = parts[0]
            v = parts[1]
            weight = int(parts[2])
            # Añadir arista al grafo
            grafo.add_edge(u, v, weight=weight)
    return grafo

# Obtener la ruta dónde se ubica este archivo
ruta = os.path.dirname(__file__)
# Unir la ruta con el nombre del archivo para leer el Grafo
ruta_grafo = os.path.join(ruta, "Grafo50.txt")
g = grafo_archivo(ruta_grafo)

# Función para crear un diccionario por si los indices son cadenas
def crear_indices(graph):
    indices = {}
    for i, nodo in enumerate(graph.nodes):
        indices[nodo] = i
    return indices

# Creación de diccionario de indices, por si los nodos son cadenas
indices = crear_indices(g)

# Función de Kruskal
def kruskal(grafo):
    # Grafo vacio que almacenará el Árbol de Recubrimiento Mínimo
    arm = nt.Graph()
    # Oredenar las aristas por su peso
    aristas = sorted(grafo.edges(data=True), key=lambda x: x[2]['weight'])
    # Creación de los conjuntos individuales por cada nodo
    conjunto = [i for i in range(len(grafo.nodes))]

    for arista in aristas:
        n1, n2, peso = arista
        # Con las siguientes líneas de código hacemos que las letras sean indices en una lista
        compu = buscar(conjunto, indices[n1])
        compv = buscar(conjunto, indices[n2])

        if compu != compv:
            fusionar(conjunto, indices[n1], indices[n2])
            arm.add_edge(n1, n2, weight = arista[2]['weight'])

    return arm

# Función para encontrar el conjunto en el que se encuentra un nodo
def buscar(conjunto, i):
    if conjunto[i] == i:
        return i
    else:
        return buscar(conjunto, conjunto[i])

# Fucnión para unir los conjuntos
def fusionar(conjunto, u, v):
    conjunto[buscar(conjunto, u)] = buscar(conjunto, v)

#Imprimir Grafos
for (u, v, p) in g.edges.data('weight'):
    print(f"({u}, {v}, {p})")

print()

arm = kruskal(g)
for (u, v, p) in arm.edges.data('weight'):
    print(f"({u}, {v}, {p})")

# Guardar Árbol de Recubrimiento Mínimo en un archivo
def guardar_grafo_archivo(arm, ruta_archivo):
    with open(ruta_archivo, 'w') as archivo:
        for (u, v, p) in arm.edges.data('weight'):
            archivo.write(f"{u},{v},{p}\n")

# Unir la ruta con el nombre del archivo para almacenar el Árbol de Recubrimiento Mínimo
ruta_resultado = os.path.join(ruta, "resultado_kruskal.txt")
guardar_grafo_archivo(arm, ruta_resultado)

# Dibujar grafo con una distribución de la libreria
pos = nt.spring_layout(g)

#edge_labels = nt.get_edge_attributes(g, 'weight')
nt.draw(g, pos, with_labels=True, node_size=100, font_size=5)
#nt.draw_networkx_edge_labels(g, pos, edge_labels, font_size=5, bbox=None, rotate=False)
mt.show()

#edge_labels_arm = nt.get_edge_attributes(arm, 'weight')
nt.draw(arm, pos, with_labels=True, node_size=100, font_size=5)
#nt.draw_networkx_edge_labels(arm, pos, edge_labels_arm, font_size=5, bbox=None, rotate=False)
mt.show()
