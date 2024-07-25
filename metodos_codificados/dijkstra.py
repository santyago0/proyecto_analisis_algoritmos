import networkx as nt
import matplotlib.pyplot as mt
import os

# Grafo desde un archivo .txt
def grafo_archivo(ruta_archivo):
    grafo = nt.DiGraph()
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
ruta_grafo = os.path.join(ruta, "Grafo30.txt")
g = grafo_archivo(ruta_grafo)

def dijkstra(G, origen):
    # Distancia más corta dese el nodo origen, se inicia con infinito
    distancias = {n: float('infinity') for n in G.nodes()}
    # Menos con el nodo origen que es 0
    distancias[origen] = 0
    # Caminos más cortos para cada nodo
    parents = {n: None for n in G.nodes()}
    
    lista_prioridades = [(0, origen)]
    
    while lista_prioridades:
        # Seleccionar el nodo con la menor distancia
        d_actual, n_actual = min(lista_prioridades, key=lambda x: x[0])
        lista_prioridades.remove((d_actual, n_actual))
        
        # Relajar aristas
        for adya, peso in G[n_actual].items():
            weight = peso['weight']
            distancia = d_actual + weight
            
            # Solo considerar distancias más cortas
            if distancia < distancias[adya]:
                distancias[adya] = distancia
                parents[adya] = n_actual
                lista_prioridades.append((distancia, adya))
    
    return distancias, parents

def arbol_recubrimiento_min(G, parents, origen):
    # Crear un grafo vacío para el Árbol de Recubrimiento Mínimo
    arm = nt.DiGraph()
    
    for node in G.nodes():
        if parents[node] is not None:
            arm.add_edge(parents[node], node, weight=G[parents[node]][node]['weight'])
    
    return arm

# Ejecutar el algoritmo de Dijkstra
origen = list(g.nodes)[0]
distancias, parents = dijkstra(g, origen)

# Construir el Árbol de Recubrimiento Mínimo
arm = arbol_recubrimiento_min(g, parents, origen)

# Imprimir Grafos
for (n1, n2, p) in g.edges.data('weight'):
    print(f"({n1}, {n2}, {p})")

print()

for (n1, n2, p) in arm.edges.data('weight'):
    print(f"({n1}, {n2}, {p})")

# Guardar Árbol de Recubrimiento Mínimo en un archivo
def guardar_grafo_archivo(arm, ruta_archivo):
    with open(ruta_archivo, 'w') as archivo:
        for (u, v, p) in arm.edges.data('weight'):
            archivo.write(f"{u},{v},{p}\n")

# Unir la ruta con el nombre del archivo para almacenar el Árbol de Recubrimiento Mínimo
ruta_resultado = os.path.join(ruta, "resultado_dijkstra.txt")
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
