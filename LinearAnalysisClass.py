import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.decomposition import FastICA as ICA
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA


class LinearAnalysisClass:
    def __init__(self, uri, citta, lab_x, lab_y):
        self.uri = uri
        self.citta = citta
        self.lab_x = lab_x
        self.lab_y = lab_y

    def readData(self):
        dataset = pd.read_csv(self.uri)
        
        return pd.DataFrame(dataset)
    
    def analysisICA(self, uno, due):
        data = self.readData()
        columns = [uno, due]
        data = data[columns].dropna()

        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data)

        ica = ICA(n_components=2, random_state=0)
        x_ica = ica.fit_transform(data_scaled)
        cmp = np.var(x_ica, axis=0)
        var = cmp/np.sum(cmp)
        titolo = f'Independent Component Analysis (ICA) su dati del dataset della mobilità urbana della {self.citta}'
        stringa = f'ICA - Dati Originali\nVarianza spiegata: {var[0]*100:.2f}% per IC1, {var[1]*100:.2f}% per IC2'

        self.chart(titolo, stringa, data_scaled, ica.components_[0 ,0], ica.components_[0, 1], x_ica, "Direzione di IC1")

    def analysisPCA(self, uno, due):
        data = self.readData()

        columns = [uno, due]
        data = data[columns].dropna()

        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data)
        
        pca = PCA(n_components=2)
        x_pca = pca.fit_transform(data_scaled)
        var = pca.explained_variance_ratio_

        titolo = f'Principal Component Analysis (PCA) su dati del dataset della mobilità urbana della {self.citta}'
        stringa = f'PCA - Dati Originali\nVarianza spiegata: {var[0]*100:.2f}% per PC1, {var[1]*100:.2f}% per PC2'

        self.chart(titolo, stringa, data_scaled, pca.components_[0, 0], pca.components_[0, 1], x_pca, "Direzione di PC1")

    def analysisLDA(self, uno, due, tre):
        data = self.readData()

        columns = [uno, due]
        x = data[columns].dropna()
        y = data.loc[x.index, tre]

        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(x)

        lda = LDA(n_components=2)
        x_lda = lda.fit_transform(data_scaled, y)
        var = lda.explained_variance_ratio_

        titolo = f'Linear Discriminat Analysis (LDA) su dati del dataset della mobilità urbana della {self.citta}'
        stringa = f'LDA - Dati Originali\nVarianza spiegata: {var[0]*100:.2f}% per LD1, {var[1]*100:.2f}% per LD2'

        plt.figure(figsize=(12, 6))

        plt.scatter(x_lda[:, 0], x_lda[:, 1], c=y.astype('category').cat.codes, cmap="autumn", alpha=0.7, label='Dati trasformati')
        plt.title(f"{titolo}\n{stringa}")
        plt.xlabel(self.lab_x)
        plt.ylabel(self.lab_y)
        plt.colorbar(label='Dati trasformati')
        plt.legend()
        plt.grid(True)
        plt.axis('equal')

        plt.subplots_adjust(top=0.85)
        plt.tight_layout()
        plt.show()

    def chart(self, titolo, stringa, data_scaled, a, b, x, lad_d):
        plt.figure(figsize=(12, 6))
        plt.suptitle(titolo)

        # Dati originali (standardizzati)
        plt.subplot(1, 2, 1)
        plt.plot(data_scaled[:, 0], data_scaled[:, 1], color="teal", alpha=0.7, label='Dati originali (standardizzati)')
        plt.quiver(0, 0, a, b, angles="xy", scale_units="xy", scale=1, label=lad_d)
        plt.title(stringa)
        plt.xlabel(self.lab_x)
        plt.ylabel(self.lab_y)
        plt.legend()
        plt.grid(True)
        # Dati trasformati
        plt.subplot(1, 2, 2)
        plt.plot(x[:, 0], x[:, 1], color="teal", alpha=0.7, label='Dati trasformati')
        plt.title(stringa)
        plt.xlabel(self.lab_x)
        plt.ylabel(self.lab_y)
        plt.legend()
        plt.grid(True)
        plt.axis("equal")
        
        plt.subplots_adjust(top=0.85)
        plt.tight_layout()
        plt.show()

"""
roma = LinearAnalysisClass("CSV/shapes.csv", "città di Roma", "shape_pt_sequence", "shape_dist_traveled")
roma.analysisPCA("shape_pt_sequence", "shape_dist_traveled")
roma.analysisICA("shape_pt_sequence", "shape_dist_traveled")
roma.analysisLDA("shape_pt_sequence", "shape_dist_traveled", "shape_id")

dublino = LinearAnalysisClass("CSV/Traffic_Flow_Data_Jan_to_June_2023_SDCC.csv", "contea di South Dublin", "Flusso", "Congestione")
dublino.analysisPCA("flow", "cong")
dublino.analysisICA("flow", "cong")
dublino.analysisLDA("flow", "cong", "day")
"""

e17 = LinearAnalysisClass("CSV/E17.csv", "Autostrda E17, tunnel Kennedy, Anversa, Belgio ", "Densità", "Velocità")
e17.analysisPCA("densita", "velocita")
e17.analysisICA("densita", "velocita")
e17.analysisLDA("densita", "velocita", "id")