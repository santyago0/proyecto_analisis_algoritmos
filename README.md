# Proyecto final de Análisis de Algoritmos
## Descripción:
En este proyecto de realiza la implementación de los siguientes algoritmos:
- **Kruskall**
- **Prim**
- **Dijkstra**

Para el desarrollo se tomó en cuenta los siguientes puntos:
- Desarrollar los algoritmos previamente mencionados del texto de Brassard.
- Desarrollar una función que permita cargar el grafo desde un archivo externo. Siendo el formato del archivo: `origen,destino,arista`.
    - [Grafo no dirigido](https://github.com/santyago0/proyecto_analisis_algoritmos/blob/main/metodos_codificados/Grafo50.txt).
    - [Grafo dirigido](https://github.com/santyago0/proyecto_analisis_algoritmos/blob/main/metodos_codificados/Grafo30.txt).
- El resultado genera un documento texto con la mismas columnas, que contenga el camino mínimo.

## Ejecución:
La carpeta *metodos_codificados* contiene los algoritmos implementados en el lenguaje de programación Python. Los algoritmos, junto con 
los archivos que contienen los grafos, deben estár en el mismo directorio, o lo que es lo mismo en la misma carpeta; de esta manera el 
código se ejecutará sin ningún inconveniente. Los archivos `resultado_dijkstra.txt`, `resultado_kruskal.txt` y `resultado_prim.txt` tienen
el camino mínimo generado por cada uno de los códigos. Estos archivos se reescriben cada vez que se ejecuten los códigos.

Otro punto a destacar de los códigos, es que estos a la hora de ejecutarlos generan dos gráficas, una del grafo original y otra del grafo 
con el camino mínimo. Cuando se genera la primera gráfica se despliega una ventana con el dibujo, esta se debe cerrar para que se genere la 
siguiente, y para finalizar la ejecución también se debe cerrar la segunda ventana con la segunda gráfica. Esto solo es para tener una 
representación visual del mismo, ya que en las indicaciones no está reflejado esto. 
