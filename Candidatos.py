#TP Final de Investigación Operativa
import numpy as np
import random
import pandas as pd

# Primero creamos un vector que genera de manera random las clasificaciones para cada categoría
candidatos_MoH = []
candidatos_clase = []
candidatos_region = []
candidatos_puntaje = []

for i in range(100):
    # Generar aleatoriamente
    genero = random.choice(["M", "H"])
    clase_alta = random.choice(["SI", "NO"])
    capital = random.choice(["SI", "NO"])
    puntaje = random.randint(1, 100)
    
    # Agregar el elemento al vector
    candidatos_MoH.append(genero)
    candidatos_clase.append(clase_alta)
    candidatos_region.append(capital)
    candidatos_puntaje.append(puntaje)

candidatos_puntaje.sort(reverse=True)

ranking = list(range(1, 101))

candidatos = np.transpose(np.array([ranking, candidatos_puntaje, candidatos_MoH, candidatos_clase, candidatos_region]))

dataset = pd.DataFrame(candidatos, columns=['Ranking','Puntaje', 'MoH', 'Clase', 'Region'])

dataset.to_csv('dataset3.csv', index=False)


