import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.decomposition import FastICA as ICA
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA


class LinearAnalysisClass:
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
        
        pca = PCA(n_components=2)
        x_pca = pca.fit_transform(data_scaled)
        var = pca.explained_variance_ratio_

        plt.figure(figsize=(12, 6))
        plt.suptitle('Principal Component Analysis (PCA) su dati del dataset della mobilità della città di Roma', fontsize=16)
        
        plt.subplot(1, 2, 1)
        plt.scatter(data_scaled[:, 0], data_scaled[:, 1], alpha=0.4, color='teal', label='Dati originali (standardizzati)')
        plt.quiver(0, 0, pca.components_[0, 0], pca.components_[0, 1], angles="xy", scale_units="xy", scale=1)
        plt.title(f'PCA - Dati Originali\nVarianza spiegata: {var[0]*100:.2f}% per PC1, {var[1]*100:.2f}% per PC2')
        plt.xlabel(columns[0])
        plt.ylabel(columns[1])
        plt.legend()
        plt.grid(True)
        plt.axis('equal')
        

        plt.subplot(1, 2, 2)
        plt.scatter(x_pca[:, 0], x_pca[:, 1], color="#86160c", label="PCA Trasformati")
        plt.title(f'PCA - Dati Trasformati\nVarianza spiegata: {var[0]*100:.2f}% per PC1, {var[1]*100:.2f}% per PC2')
        plt.xlabel("PC1")
        plt.ylabel("PC2")
        plt.legend()
        plt.grid(True)
        plt.axis('equal')

        plt.subplots_adjust(top=0.85)
        plt.tight_layout()
        plt.show()

    def chartWithLDA(self):
        data = self.readCSV()

        columns = ["shape_pt_sequence", "shape_dist_traveled"]
        x = data[columns].dropna()
        y = data.loc[x.index, "shape_id"]

        scaler = StandardScaler()
        x_scaled = scaler.fit_transform(x)

        lda = LDA(n_components=2)
        x_lda = lda.fit_transform(x_scaled, y)
        var = lda.explained_variance_ratio_
        
        plt.figure(figsize=(12, 6))
        plt.suptitle('Linear Discriminat Analysis (LDA) su dati del dataset della mobilità della città di Roma', fontsize=16)

        plt.subplot(1, 2, 1)
        plt.scatter(x_scaled[:, 0], x_scaled[:, 1], alpha=0.4, color='teal', label='Dati originali (standardizzati)')
        plt.quiver(0, 0, lda.coef_[0, 0], lda.coef_[0, 1], color='black', label='Direzione LD1')
        plt.title(f'LDA - Dati Originali\nVarianza spiegata: {var[0]*100:.2f}% per LD1, {var[1]*100:.2f}% per LD2')
        plt.xlabel(columns[0])
        plt.ylabel(columns[1])
        plt.legend()
        plt.grid(True)
        plt.axis('equal')
        
        plt.subplot(1, 2, 2)
        plt.scatter(x_lda[:, 0], x_lda[:, 1], c=y.astype('category').cat.codes, cmap="autumn", alpha=0.7, label='LDA Trasformati')
        plt.title(f'LDA - Dati Trasformati\nVarianza spiegata: {var[0]*100:.2f}% per LD1, {var[1]*100:.2f}% per LD2')
        plt.xlabel("LD1")
        plt.ylabel("LD2")
        plt.legend()
        plt.grid(True)
        plt.axis('equal')

        plt.subplots_adjust(top=0.85)
        plt.tight_layout()
        plt.show()
    
    def chartWithICA(self):
        data = self.readCSV()
        columns = ["shape_pt_sequence", "shape_dist_traveled"]
        data = data[columns].dropna()

        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data)

        ica = ICA(n_components=2, random_state=0)
        x_ica = ica.fit_transform(data_scaled)
        cmp = np.var(x_ica, axis=0)
        var = cmp/np.sum(cmp)

        plt.figure(figsize=(12, 6))
        plt.suptitle('Independent Component Analysis (ICA) su dati del dataset della mobilità della città di Roma', fontsize=16)
        
        plt.subplot(1, 2, 1)
        plt.scatter(data_scaled[:, 0], data_scaled[:, 1], alpha=0.4, color='teal', label='Dati originali (standardizzati)')
        plt.quiver(0, 0, ica.components_[0, 0], ica.components_[0, 1], angles="xy", scale_units="xy", scale=1)
        plt.title(f'ICA - Dati Originali\nVarianza spiegata: {var[0]*100:.2f}% per PC1, {var[1]*100:.2f}% per PC2')
        #plt.title('ICA - Dati Originali')
        plt.xlabel(columns[0])
        plt.ylabel(columns[1])
        plt.legend()
        plt.grid(True)
        plt.axis('equal')
        plt.subplot(1, 2, 2)
        plt.scatter(x_ica[:, 0], x_ica[:, 1], color="#86160c", label="PCA Trasformati")
        plt.title(f'ICA - Dati Trasformati\nVarianza spiegata: {var[0]*100:.2f}% per PC1, {var[1]*100:.2f}% per PC2')
        #plt.title('ICA - Dati Trasformati')
        plt.xlabel("IC1")
        plt.ylabel("IC2")
        plt.legend()
        plt.grid(True)
        plt.axis('equal')

        plt.subplots_adjust(top=0.85)
        plt.tight_layout()
        plt.show()

linear = LinearAnalysisClass()
linear.chartWithPCA()
linear.chartWithLDA()
linear.chartWithICA()