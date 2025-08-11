# Analisi dei Percorsi Minimi in una Rete Multinodo
## File
- Dijkstra.py

## Descrizione

Questo progetto consente di analizzare i costi di percorrenza all'interno di una rete di trasporto composta da più nodi e archi ponderati. Utilizza l'algoritmo di Dijkstra su grafi non orientati per trovare i cammini minimi da diverse sorgenti e determina la configurazione più efficiente in termini di costo.

## Obiettivo

Determinare quale combinazione di nodi sorgente (A, B, C, AB, AC, BC, ABC) garantisce il costo totale minimo considerando:
- il costo fisso associato al nodo o combinazione di nodi
- la somma dei cammini minimi verso tutti gli altri nodi

## Problema
![alt text](image002.png)

![alt text](image003.png)

![alt text](image004.png)


# Tecniche di pre-processing e pulizia dei dati

## Descrizione

Le tecniche di processing e pulizia dei dati hanno l’obiettivo di correggere eventuali errori, trattare i dati mancanti, uniformandone il formato. Inoltre, aiutano a selezionare le variabili più rivelanti e a ridurre la dimensionalità della struttura dei dati, per un’analisi più efficiente, migliorando le presta-zioni dei modelli.

## Tecniche linerari
- Principal Component Analysis (PCA)
- Linear Discriminat Analysis (LDA)
- Independent Component Analysis (ICA)

## File 
- LinearAnalysisClass.py

## Dataset

- [Traffic Flow Data Jan to June 2023 SDCC](https://data.smartdublin.ie/dataset/traffic-flow-data-jan-to-june-2023-sdcc1)
- [Mobilità urbana della città di Roma](https://romamobilita.it/it/tecnologie/open-data)

# Modello Lighthill Whitham Richards

## Descrizione

Analisi macroscopica con il modello Lighthill Whitham Richards nei pressi dell'autostrada E17 nelle vicinanze del tunnel Kennedy ad Anversa in Belgio con dati estratti con una simulazione con il software SUMO (Simulation of Urban Mobility).

## File
- LighthillWhithamRichards.py

## Tecnologie Utilizzate

- Python 3
- [NetworkX](https://networkx.org/) — per la creazione e l'analisi del grafo
- [Matplotlib](https://matplotlib.org/) — per la visualizzazione del grafo
- [OSM Web Wizard](https://www.openstreetmap.org/#map=) — crea mappe personalizzate
- [Pandas](https://pandas.pydata.org/) — per la gestione dei dati da file CSV
- [Sklearn](https://scikit-learn.org/stable/) per la riduzione della dimensionalità dei dati
- [SUMO (Simulation of Urban Mobility)](https://sumo.dlr.de/docs/index.html) — Software per la simulazione della mobilità urbana

```bash
git clone https://github.com/tumminia/PLI