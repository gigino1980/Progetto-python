import sys
import numpy as np

print("Ciao Gigino!")
print("Progetto Python avviato")

print("Versione Python:", sys.version)
print("Ambiente:", sys.executable)
print("sistema operativo:", sys.platform) 

numeri = np.array([10, 20, 30, 40, 50])

print("Array:", numeri)
print("Media:", np.mean(numeri))