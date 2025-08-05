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

    def chart(self, d_osservata, f_osservato, d_simulata, f_simulato):

        plt.figure(figsize=(12, 6))
        plt.suptitle("Contronto tra flusso osservato e modello LWR")

        plt.subplot(1, 2, 1)
        plt.plot(d_osservata, f_osservato, alpha=0.7, color='teal', label=f'Flusso osservato')
        plt.title("Flusso osservato")
        plt.xlabel("Densità (veicoli/km)")
        plt.ylabel("Flusso (veicoli/km)")
        plt.legend()
        plt.grid(True)

        plt.subplot(1, 2, 2)
        plt.plot(d_simulata, f_simulato, alpha=0.7, color="red", label="Flusso simulato (LWR)")
        plt.title("Flusso simulato (LWR)")
        plt.xlabel("Densità (veicoli/km)")
        plt.ylabel("Flusso (veicoli/km)")
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()

    def analizzaTraffico(self):
        data = self.leggiDati()
        num_celle = len(data)
        x = 690.0
        dx = x/(num_celle - 1)
        dt = 0.01
        rho_max = 150.0
        v_max = 70 * (1/3.6)
        densita = data['densita'].to_numpy()

        if v_max  * (dt/dx)>1:
            raise ValueError(f"Condizione CFL non soddisfatta: ridurre dt o aumentare dx")


        #for t in tempo:
        for _ in range(100):
            velocita =self.calcolaVelocita(densita, rho_max, v_max)
            flusso = densita * velocita
            densita = self.conservazione(num_celle, densita, flusso, dx, dt)
        
        self.stampaStatoTraffico(densita, flusso)
        self.chart(data['densita'].to_list(), data["flusso"].to_list(), densita, flusso)

lwr = LighthillWhithamRichards()
lwr.analizzaTraffico()