from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt


class Clustering:
    def __init__(self, uri):
        self.uri = uri

    def readCSV(self):
        dataset = pd.read_csv(self.uri)

        return pd.DataFrame(dataset)
    
    def kmeans_algorithm(self, uno, due):
        dataset = self.readCSV()
        columns = [uno, due]
        x = dataset[columns].dropna()
        scaler = StandardScaler()
        x_scaled = scaler.fit_transform(x)
        kmeans = KMeans(n_clusters=2, random_state=42)
        y_kmeans = kmeans.fit_predict(x_scaled)

        # Visualizzazione dei cluster
        plt.subplot(1, 2, 1)
        plt.scatter(x_scaled[:, 0], x_scaled[:, 1], c=y_kmeans, cmap='viridis')
        plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='X')
        plt.title('Clustering con K-Means')
        plt.xlabel('Densità')
        plt.ylabel('Velocità')

        plt.subplot(1, 2, 2)
        # Applicazione del PCA
        pca = PCA(n_components=2)
        x_pca = pca.fit_transform(x_scaled)
        
        # Visualizzazione delle componenti principali
        plt.scatter(x_pca[:, 0], x_pca[:, 1], c=y_kmeans, cmap='viridis')
        plt.title('Riduzione della Dimensionalità con PCA')
        plt.xlabel('Densità')
        plt.ylabel('Velocità')

        plt.show()

clustering = Clustering("CSV/lwr/E17.csv")
clustering.kmeans_algorithm("densita", "velocita")