# Analisi dei Percorsi Minimi in una Rete Multinodo
## File Dijkstra.py

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

Le tecniche di processing e pulizia dei dati hanno l’obiettivo di correggere eventuali errori, trattare i dati mancanti, uniformandone il formato. Inoltre, aiutano a selezionare le variabili più rivelanti e a ridurre la dimensionalità della struttura dei dati, per un’analisi più efficiente, migliorando le presta-zioni dei modelli.

## Tecniche linerari
- Principal Component Analysis (PCA)
- Linear Discriminat Analysis (LDA)
- Independent Component Analysis (ICA)

## File 
- LinearAnalysisClass.py

## Tecniche non lineari


## Dataset

- [Mobilità urbana della città di Roma](https://romamobilita.it/it/tecnologie/open-data)

## Tecnologie Utilizzate

- Python 3
- [NetworkX](https://networkx.org/) — per la creazione e l'analisi del grafo
- [Matplotlib](https://matplotlib.org/) — per la visualizzazione del grafo
- [Pandas](https://pandas.pydata.org/) — per la gestione dei dati da file CSV

```bash
git clone https://github.com/tumminia/PLI