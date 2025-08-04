import pandas as pd
import matplotlib.pyplot as plt

class LighthillWhithamRichards:
    
    def leggiDati(self):
        dataset = pd.read_csv("CSV/E17.csv")

        return pd.DataFrame(dataset)
    
    def calcolaVelocita(self, rho, rho_max=1.0, v_max=150):
        return  v_max * (1 - rho/rho_max)
    
    def conservazione(self, num_celle, densita, flusso, x, t):
        nuova_densita = densita.copy()

        for item in range(1, num_celle-1):
            f = (flusso[item] - flusso[item - 1])/x
            nuova_densita[item] = densita[item] - t * f

            if nuova_densita[item]<0:
                nuova_densita[item] = 0
            
        return nuova_densita
    
    def stampaStatoTraffico(self,  densita, flusso, tempo):
        for i in range(len(densita)):
            print(f"Tempo: {tempo[i]}\nDensità: {densita[i]}\nFlusso: {flusso[i]}\n")

    def chart(self, d_osservata, f_osservato, d_simulata, f_simulato):

        plt.figure(figsize=(12, 6))
        plt.suptitle("Contronto tra flusso osservato e modello LWR")

        plt.subplot(1, 2, 1)
        plt.plot(d_osservata, f_osservato, alpha=0.7, color='teal', label=f'Flusso osservato')
        plt.title(f"Flusso osservato")
        plt.xlabel("Densità (veicoli/km)")
        plt.ylabel("Flusso (veicoli/km)")
        plt.legend()
        plt.grid(True)

        plt.subplot(1, 2, 2)
        plt.plot(d_simulata, f_simulato, alpha=0.7, color="red", label="Flusso simulato (LWR)")
        plt.title(f"Flusso simulato (LWR)")
        plt.xlabel("Densità (veicoli/km)")
        plt.ylabel("Flusso (veicoli/km)")
        plt.legend()
        plt.grid(True)

        #plt.axis("equal")
        plt.tight_layout()
        plt.show()


    def analizzaTraffico(self):
        data = self.leggiDati()
        num_celle = len(data)
        x = 1.0
        t = 0.01
        rho_max = 1.0
        densita = data['densita'].to_list()
        tempo = data['t'].to_list()

        #for t in tempo:
        for _ in range(100):
            flusso = [d * self.calcolaVelocita(d, rho_max) for d in densita]
            densita = self.conservazione(num_celle, densita, flusso, x, t)
            
        self.stampaStatoTraffico(densita, flusso, tempo)

        self.chart(data['densita'].to_list(), data["flusso"].to_list(), densita, flusso)

lwr = LighthillWhithamRichards()
lwr.analizzaTraffico()