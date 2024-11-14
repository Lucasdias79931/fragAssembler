import os
import re

here = os.path.dirname(os.path.abspath(__file__))

headersPath = os.path.join(here, "CDSsPreparados/cds.fasta")

headers = list()

coordenadas = list()

try:

    with open(headersPath, "r") as file:
        for line in file:
            if line.startswith(">"):
                headers.append(line.strip().replace(">", ""))

except FileNotFoundError as e:
    print(e)
    exit(1)
except Exception as e:
    print(f"Erro inesperado: {e}")
    exit(1) 

for header in headers:
    padrao = r"([cC]?\d+)-(\d+)"
    resultados = re.findall(padrao, header)

    if resultados:
        if resultados[0][0].startswith("c"):
            coordenadas.append([int(resultados[0][0].replace("c", "")), int(resultados[0][1])])
        else:
            coordenadas.append([int(resultados[0][0]), int(resultados[0][1])])

for coordenada in coordenadas:

    if coordenada[0] > coordenada[1]:
        
        print(f"Coordenada invalida: {coordenada}")
        exit(1)
    else:
        print("coordenada válida")

for i in range(len(coordenadas) - 1):
    if coordenadas[i][1] > coordenadas[i][0]:
        print(f"Coordenada invalida: {coordenadas[i] } {coordenadas[i + 1]}")
        print(coordenadas[i +1][0] - coordenadas[i][1])
        exit(1)