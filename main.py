
import customtkinter as ctk
import tkinter as tk 
# Configurazione grafica
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Creazione finestra principale
app = ctk.CTk()

app.title("La mia prima applicazione")
app.geometry("600x450")
app.resizable(False,False)

# Titolo
titolo = ctk.CTkLabel(
    app,
    text="Apicoltura Sancilio",
    font=("Arial", 26, "bold")
)
titolo.pack(pady=30)

titolo1 = ctk.CTkLabel(
    app,
    text="Apicoltura Loredana",
    font=("Arial", 26, "bold")
)
titolo1.pack(pady=20)

# Campo di inserimento nome
nome = ctk.CTkEntry(
    app,
    placeholder_text="Inserisci l'arnia o il nome della regina",
    width=300,
    height=40
)
nome.pack(pady=10)

# Campo di inserimento numero
quantita = ctk.CTkEntry(
    app,
    placeholder_text="Inserisci quantità",
    width=300,
    height=40
)
quantita.pack(pady=10)

# Etichetta risultato
risultato = ctk.CTkLabel(
    app,
    text="In attesa di dati...",
    font=("Arial", 16)
)
risultato.pack(pady=20)

# Funzione del pulsante
def salva_dati():
    nome_inserito = nome.get()
    quantita_inserita = quantita.get()

    risultato.configure(
        text=f"Nome: {nome_inserito} | Quantità: {quantita_inserita}"
    )

def mostra():
    risultato.configure(
        text=f"Ciao",  
    )

# Pulsante SALVA
pulsante = ctk.CTkButton(
    app,
    text="SALVA DATI",
    width=200,
    height=40,
    command=salva_dati
)
pulsante.pack(pady=10)

# Pulsante SALVA
pulsante1 = ctk.CTkButton(
    app,
    text="Mostra ",
    width=200,
    height=40,
    command=mostra
)
pulsante1.pack(pady=10)

# Avvio applicazione
app.mainloop()
