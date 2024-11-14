import os
import re

here = os.path.dirname(os.path.abspath(__file__))

sequencePath = os.path.join(here, "chromosome1HomoSapien/reversedSequence.fasta")

cdsPath = os.path.join(here, "CDSsPreparados/cdsInC.fasta")



sequence = ''
coordenadas = list()

seqs = list()

try:

    
    with open(sequencePath, "r") as file:
        seq = []
        for line in file:
            if not line.startswith(">"):
                seq.append(line.strip())
        
        sequence = ''.join(seq)

    with open(cdsPath, "r") as file:
        seq = []
        for line in file:
            if not line.startswith(">"):
                seqs.append(line.strip())

            
        


except FileNotFoundError as e:
    print(e)
    exit(1)
except Exception as e:
    print(f"Erro inesperado: {e}")
    exit(1) 


for segment in seqs:
    if not segment in sequence:
        print("Segmento inexistente")
        exit(1)
print("Sequência obtida com sucesso")