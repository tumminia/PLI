import pandas as pd
import matplotlib.pyplot as plt

# La classe  LighthillWhithamRichards contiene tutti metodi per l’analisi e implementazione del modello LWR
class LighthillWhithamRichards:
    # legge i da un file .csv
    def leggiDati(self, uri):
        dataset = pd.read_csv(uri)

        return pd.DataFrame(dataset)
    
    # calcola la velocità in funzione della densità
    def calcolaVelocita(self, rho, rho_max, v_max):
        return  v_max * (1 - rho/rho_max)
    
    # implementa la legge della conservazione 
    def conservazione(self, num_celle, densita, flusso, dx, dt):
        # fa una copia della densità, non sovrascrivendola
        nuova_densita = densita.copy()

        # aggiorna la densità in ogni cella
        for item in range(1, num_celle-1):
            f = (flusso[item] - flusso[item - 1])/dx
            nuova_densita[item] = densita[item] - dt * f

            if nuova_densita[item]<0:
                nuova_densita[item] = 0
        
        nuova_densita[0] = densita[0]
        nuova_densita[-1] = densita[-1]

        return nuova_densita
    
    # stampa a video la densità e il flusso nel periodo t
    def stampaStatoTraffico(self,  densita, flusso):
        for i in range(len(densita)):
            print(f"Tempo: {i}\nDensità: {densita[i]}\nFlusso: {flusso[i]}\n")
    
    #crea un grafico della densità e del flusso nel periodo t
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
    
    # estrae e analizza i dati
    def analizzaTraffico(self, uri, v):
        data = self.leggiDati(uri) # legge dati
        num_celle = len(data)
        dx = 8000.0 # distanza in metri
        v_max = v * (1/3.6) # velocità massima, converte da km/h a m/s
        dt = dx/v_max # tempo per percorrere dx
        c_max = 3600/dt # capacità massima (veicoli/ora/corsia)
        rho_max = c_max/v_max # densità massima
        
        densita = data["densita"].to_list()
        #calcola il flusso
        data["flusso"] =  data["densita"] * data["velocita"]
        
        # controlla la condizione CFL, che deve avere un valore minore uguale a 1
        if v_max  * (dt/dx)>1:
            raise ValueError(f"Condizione CFL non soddisfatta: ridurre dt o aumentare dx")
        
        for _ in range(100):
            # calcola velocità di ogni cella
            velocita = [self.calcolaVelocita(d, rho_max, v_max) for d in densita]
            # aggiorna il flusso
            flusso = [d * v for d,v in zip(densita, velocita)]
            # aggiorna la densità con l'equazione della conservazione
            densita = self.conservazione(num_celle, densita, flusso, dx, dt) 
        
        # stampa a video i risultati della simulazione
        self.stampaStatoTraffico(densita, flusso)
        # crea un grafico della densità e del flusso dei dati dal file csv
        self.chart(
            data["densita"].to_list(),
            data["flusso"].to_list(),
            data["t"].to_list(),
            "Densità e Flusso del traffico in periodo di tempo t"
        )
        # crea un grafico della densità e del flusso, estrapolati dalla simulazione
        self.chart(
            densita,
            flusso,
            data["t"].to_list(),
            "Modello Lighthill Whitham Richards applicato sull'autostrada E17, tunnel Kennedy, Anversa, Belgio"
        )

lwr = LighthillWhithamRichards()
lwr.analizzaTraffico("CSV/E17_flusso_alto.csv", 25)
lwr.analizzaTraffico("CSV/E17_flusso_medio.csv", 50)
lwr.analizzaTraffico("CSV/E17_flusso_basso.csv", 120)