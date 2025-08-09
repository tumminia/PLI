import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

class LighthillWhithamRichards:    
    def leggiDati(self, uri):
        dataset = pd.read_csv(uri)

        return pd.DataFrame(dataset)
    
    def calcolaVelocita(self, rho, rho_max, v_max):
        return  v_max * (1 - rho/rho_max)
    
    def conservazione(self, num_celle, densita, flusso, dx, dt):
        nuova_densita = densita.copy()

        for item in range(1, num_celle-1):
            f = (flusso[item] - flusso[item - 1])/dx
            nuova_densita[item] = densita[item] - dt * f

            if nuova_densita[item]<0:
                nuova_densita[item] = 0
        
        nuova_densita[0] = densita[0]
        nuova_densita[-1] = densita[-1]

        return nuova_densita
    
    def stampaStatoTraffico(self,  densita, flusso):
        for i in range(len(densita)):
            print(f"Tempo: {i}\nDensità: {densita[i]}\nFlusso: {flusso[i]}\n")

    def chart(self, densita, flusso, periodo, titolo):
        plt.figure(figsize=(12, 6))
        plt.suptitle(titolo)

        plt.subplot(1, 2, 1)
        plt.plot( periodo, densita, alpha=0.7, color='teal', label="Densità in un periodo t(s)")
        plt.title("Densità in un periodo di tempo t(s)")
        plt.xlabel("Tempo in periodo da 0 a t (s)")
        plt.ylabel("Densità (veicoli/km)")
        plt.legend()
        plt.grid(True)

        plt.subplot(1, 2, 2)
        plt.plot(periodo, flusso, alpha=0.7, color="red", label="Flusso in un periodo t(s)")
        plt.title("Flusso in un periodo di tempo t(s)")
        plt.xlabel("Tempo in periodo da 0 a t (s)")
        plt.ylabel("Flusso (veicoli/km)")
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()

    def analizzaTraffico(self, uri, v):
        data = self.leggiDati(uri)
        num_celle = len(data)
        x = 8000.0
        dx = x#/(num_celle - 1)
        dt = 1
        rho_max = 150.0
        v_max = v * (1/3.6)
        
        densita = data["densita"].to_numpy()
        data["flusso"] =  data["densita"] * data["velocita"]

        if v_max  * (dt/dx)>1:
            raise ValueError(f"Condizione CFL non soddisfatta: ridurre dt o aumentare dx")
        
        for _ in range(100):
            velocita = self.calcolaVelocita(densita, rho_max, v_max)
            flusso = densita * velocita
            densita = self.conservazione(num_celle, densita, flusso, dx, dt)
        
        #self.stampaStatoTraffico(densita, flusso)
        
        self.chart(
            data["densita"].to_list(),
            data["flusso"].to_list(),
            data["t"].to_list(),
            "Densità e Flusso del traffico in periodo di tempo t"
        )
        self.chart(
            densita,
            flusso,
            data["t"].to_list(),
            "Modello Lighthill Whitham Richards applicato sull'autostrada E17, tunnel Kennedy, Anversa, Belgio"
        )

lwr = LighthillWhithamRichards()
lwr.analizzaTraffico("CSV/E17_flusso_alto.csv", 34)
lwr.analizzaTraffico("CSV/E17_flusso_medio.csv", 72)
lwr.analizzaTraffico("CSV/E17_flusso_basso.csv", 120)
