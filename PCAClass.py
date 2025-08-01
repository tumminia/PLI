import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

class PCAClass:
    def readCSV(self):
        dataset = pd.read_csv("CSV/shapes.csv")
        data = pd.DataFrame(dataset)

        return data

    def chartWithPCA(self):
        data = self.readCSV()

        columns = ["shape_pt_sequence", "shape_dist_traveled"]
        data = data[columns].dropna()

        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data)
        
        pca = PCA(n_components=1)
        X_pca = pca.fit_transform(data_scaled)
        X_reconstructed = pca.inverse_transform(X_pca)
        
        plt.figure(figsize=(8, 6))
        plt.scatter(data_scaled[:, 0], data_scaled[:, 1], alpha=0.4, label='Dati originali (standardizzati)')
        plt.scatter(X_reconstructed[:, 0], X_reconstructed[:, 1], alpha=0.7, label='Dati ricostruiti (1 componente)')
        plt.plot([0, pca.components_[0, 0]], [0, pca.components_[0, 1]], color='red', label='Direzione PC1')
        plt.title('PCA su dati Roma (MongoDB)')
        plt.xlabel(columns[0])
        plt.ylabel(columns[1])
        plt.legend()
        plt.grid(True)
        plt.axis('equal')
        plt.show()

pcaClass = PCAClass()
pcaClass.chartWithPCA()