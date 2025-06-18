import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

class Dijkstra:
    def __init__(self,item, sources, nodi):
        self.G = nx.Graph()    
        self.G.add_nodes_from(item)
        self.sources = sources
        self.edges = [(row['input'], row['output'], row['arco']) for _, row in nodi.iterrows()]

        for i, o, arco in self.edges:
            self.G.add_edge(i, o, weight=arco)
        
    # trova il cammino (archi) più breve 
    def cammino_minimo(self,str):
        paths = nx.multi_source_dijkstra_path(self.G, sources=self.sources, weight="weight")
        print(f"Analizza il cammino minimo di {str}")

        for target, path in paths.items():
            print(f"Percorso da {self.sources} a {target}: {path}")
        
        print("\n")
        
    # Tramite algoritmo Dijkstra trovo il cammino (archi) di ogni nodo
    def costo_minimo(self, str, x):
        print(f"{str}") 
        distances = nx.multi_source_dijkstra_path_length(self.G, sources=self.sources, weight="weight")
        totale = 0

        # somma il costo di cammino
        for target, distance in distances.items():
            if distance>0:
                print(f"Percorso da {self.sources} a {target}: {distance}")
                totale +=distance
        
        # sommo il costo del nodo con il costo totale dei cammini (archi) 
        x += totale
        print(f"Costo totale: {x}\n")
        return x

    # crea grafico dei nodi e degli archi
    def grafico(self, pos):
        # Visualizziamo il grafo
        # pos = nx.spring_layout(self.G)
        
        nx.draw(self.G, pos, with_labels=True, node_size=2000, node_color='lightblue', edge_color='red')
        
        nodi_labels = {(i, o): d['weight'] for i, o, d in self.G.edges(data=True)}
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=nodi_labels)
        
        plt.show()

# Aggiungiamo gli archi (strade o tratte di trasporto pubblico) con costi (tempi di percorrenza)
nodiA = pd.read_csv("CSV/a.csv")
nodiB = pd.read_csv("CSV/b.csv")
nodiC = pd.read_csv("CSV/c.csv")
nodiAB = pd.read_csv("CSV/ab.csv")
nodiAC = pd.read_csv("CSV/ac.csv")
nodiBC = pd.read_csv("CSV/bc.csv")
nodiABC = pd.read_csv("CSV/abc.csv")

itemA = ["A", "W", "X", "Y", "Z"]
itemB = ["B", "W", "X", "Y", "Z"]
itemC = ["C", "W", "X", "Y", "Z"]
itemAB = ["A", "B", "W", "X", "Y", "Z"]
itemAC = ["A", "B", "W", "X", "Y", "Z"]
itemBC = ["B", "C", "W", "X", "Y", "Z"]
itemABC = ["A", "B", "C", "W", "X", "Y", "Z"]

F = [{"A":4, "B":5, "C":10, "AB":9, "AC":14, "BC":15, "ABC":19}]
sourcesA = ["A"]
sourcesB = ["B"]
sourcesC = ["C"]
sourcesAB = ["A", "B"]
sourcesAC = ["A", "C"]
sourcesBC = ["B", "C"]
sourcesABC = ["A", "B", "C"]

array = [{'A':0}, {'B':0}, {'C':0}, {'AB':0}, {'AC':0}, {'BC':0}, {'ABC':0}]

print("\n\n")

camminiNodoA = Dijkstra(item=itemA, sources=sourcesA, nodi=nodiA)
camminiNodoB = Dijkstra(item=itemB, sources=sourcesB, nodi=nodiB)
camminiNodoC = Dijkstra(item=itemC, sources=sourcesC, nodi=nodiC)
camminiNodiAB = Dijkstra(item=itemAB, sources=sourcesAB, nodi=nodiAB)
camminiNodiAC = Dijkstra(item=itemAC, sources=sourcesAC, nodi=nodiAC)
camminiNodiBC = Dijkstra(item=itemBC, sources=sourcesBC, nodi=nodiBC)
camminiNodiABC = Dijkstra(item=itemABC, sources=sourcesABC, nodi=nodiABC)

camminiNodoA.cammino_minimo("A")
camminiNodoB.cammino_minimo("B") 
camminiNodoC.cammino_minimo("C")
camminiNodiAB.cammino_minimo("A e B")
camminiNodiAC.cammino_minimo("A e C")
camminiNodiBC.cammino_minimo("B e C")
camminiNodiABC.cammino_minimo("A, B e C")

array[0]['A'] = camminiNodoA.costo_minimo("Analizza il nodo A", x=F[0]['A'])
array[1]['B'] = camminiNodoB.costo_minimo("Analizza il nodo B", x=F[0]['B']) 
array[2]['C'] = camminiNodoC.costo_minimo("Analizza il nodo C", x=F[0]['C'])
array[3]['AB'] = camminiNodiAB.costo_minimo("Analizza i nodi A e B", x=F[0]['AB'])
array[4]['AC'] = camminiNodiAC.costo_minimo("Analizza i nodi A e C", x=F[0]['AC'])
array[5]['BC'] = camminiNodiBC.costo_minimo("Analizza i nodi B e C", x=F[0]['BC'])
array[6]['ABC'] = camminiNodiABC.costo_minimo("Analizza i nodi A, B e C", x=F[0]['ABC'])

min_value = float('inf')
config_min_costo = None

for obj in array:
    for key, value in obj.items():
        if value < min_value:
            min_value = value
            config_min_costo = key

print(f"Costo minore: {config_min_costo} = {min_value}")

posABC = {
    'A': (0, 4),
    'B': (0, 2),
    'C': (0, 0),
    'W': (-1, 2),
    'X': (-1, 1),
    'Y': (1, 2),
    'Z': (1, 1),
}
camminiNodiABC.grafico(pos=posABC)