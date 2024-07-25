import networkx as nt
import matplotlib.pyplot as mt
import os

# Grafo desde un archivo .txt
def grafo_archivo(ruta_archivo):
    grafo = nt.Graph()
    with open(ruta_archivo) as archivo:
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
# Unir la ruta con el nombre del archivo para leer el Grafo
ruta = os.path.dirname(__file__)
ruta_grafo = os.path.join(ruta, "Grafo50.txt")
g = grafo_archivo(ruta_grafo)

def prim(G):
    # Grafo vacío que almacenará el Árbol de Recubrimiento Mínimo
    arm = nt.Graph()
    # Conjunto de nodos recorridos
    conjunto = set()

    # Seleccionar un nodo inicial, en este caso el primero
    nodo_inicio = list(G.nodes())[0]
    conjunto.add(nodo_inicio)

    # Lista de las aristas conectadas al nodo inicial
    aristas = [(data['weight'], nodo_inicio, nodo_destino) for nodo_destino, data in G[nodo_inicio].items()]
    # Ordena las aristas por el peso
    aristas.sort(key=lambda x: x[0])

    # Mientras el conjunto contenga aristas
    while aristas:
        weight, u, v = aristas.pop(0) # Obtiene la arista de menos peso
        # Si el nodo 'v' no se encuentra en el conjunto:
        if v not in conjunto:
            # Se añade al conjunto
            conjunto.add(v)
            # Se añade al Árbol de Recubrimiento Mínimo
            arm.add_edge(u, v, weight=weight)

            # Añadir todas las aristas conectadas al nodo 'v' que no están en el conjunto
            for arista_v, peso in G[v].items():
                if arista_v not in conjunto:
                    aristas.append((peso['weight'], v, arista_v))
            
            # Ordenar las aristas por peso después de añadir nuevas aristas
            aristas.sort(key=lambda x: x[0])

    return arm

# Imprimir Grafos
for (n1, n2, p) in g.edges.data('weight'):
    print(f"({n1}, {n2}, {p})")

print()

arm = prim(g)
for (n1, n2, p) in arm.edges.data('weight'):
    print(f"({n1}, {n2}, {p})")

# Guardar Árbol de Recubrimiento Mínimo en un archivo
def guardar_grafo_archivo(arm, ruta_archivo):
    with open(ruta_archivo, 'w') as archivo:
        for (u, v, p) in arm.edges.data('weight'):
            archivo.write(f"{u},{v},{p}\n")

# Unir la ruta con el nombre del archivo para almacenar el Árbol de Recubrimiento Mínimo
ruta_resultado = os.path.join(ruta, "resultado_prim.txt")
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
