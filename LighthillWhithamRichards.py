import pandas as pd
import matplotlib.pyplot as plt

class LighthillWhithamRichards:
    
    def leggiDati(self):
        dataset = pd.read_csv("CSV/E17.csv")

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

    def chart(self, d_1, f_1, d_2, f_2, titolo, tit_1, tit_2, lab_x1, lab_x2, lab_y):

        plt.figure(figsize=(12, 6))
        plt.suptitle(titolo)

        plt.subplot(1, 2, 1)
        plt.plot(d_1, f_1, alpha=0.7, color='teal', label=lab_x1)
        plt.title(tit_1)
        plt.xlabel(lab_x1)
        plt.ylabel(lab_y)
        plt.legend()
        plt.grid(True)

        plt.subplot(1, 2, 2)
        plt.plot(d_2, f_2, alpha=0.7, color="red", label=lab_x2)
        plt.title(tit_2)
        plt.xlabel(lab_x2)
        plt.ylabel(lab_y)
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()

    def analizzaTraffico(self):
        data = self.leggiDati()
        num_celle = len(data)
        x = 8000.0
        dx = x/(num_celle - 1)
        dt = 0.01
        rho_max = 150.0
        v_max = 120 * (1/3.6)
        densita = data['densita'].to_numpy()

        if v_max  * (dt/dx)>1:
            raise ValueError(f"Condizione CFL non soddisfatta: ridurre dt o aumentare dx")
        
        for _ in range(100):
            velocita =self.calcolaVelocita(densita, rho_max, v_max)
            flusso = densita * velocita
            densita = self.conservazione(num_celle, densita, flusso, dx, dt)
        
        self.stampaStatoTraffico(densita, flusso)
        self.chart( data['densita'].to_list(), data["flusso"].to_list(),
             densita, flusso,
             "Contronto tra flusso osservato e modello LWR",
             "Flusso osservato",
             "Flusso simulato (LWR)",
             "Densità (veicoli/km)",
             "Densità (veicoli/km)",
             "Flusso (veicoli/km)"
            )
        self.chart( data['t'].to_list(), data['densita'].to_list(),
             data['t'].to_list(), data["flusso"].to_list(),
             "Modello Lighthill Whitham Richards",
             "Densità",
             "Flusso",
             "Densità (veicoli/km)",
             "Flusso (veicoli/km)",
             "Tempo in periodo da 0 a t (s)"
            )
        self.chart( data['t'].to_list(), densita,
             data['t'].to_list(), flusso,
             "Modello Lighthill Whitham Richards",
             "Densità",
             "Flusso",
             "Densità (veicoli/km)",
             "Flusso (veicoli/km)",
             "Tempo in periodo da 0 a t (s)"
            )

lwr = LighthillWhithamRichards()
lwr.analizzaTraffico()