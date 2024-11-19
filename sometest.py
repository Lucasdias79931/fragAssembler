import os
from prepareCDSs import PrepareCDSs 


here = os.path.dirname(os.path.abspath(__file__))

cdsDestinePath = os.path.join(here, "CDSsPreparados","cds.fasta")
cdsCDestinePath = os.path.join(here, "CDSsPreparados","cdsInC.fasta")
prepCds = PrepareCDSs()
prepCds.sequence = prepCds.getSequence(os.path.join(here, "chromosome1HomoSapien/sequence.fasta"))
prepCds.complement  = prepCds.getSequence(os.path.join(here, "chromosome1HomoSapien/reversedSequence.fasta"))

#for i in range(1, 39):
prepCds.getSequence(os.path.join(here, f"chromosome1HomoSapien/CDS{2}.fasta"), True)

prepCds.getCoordenadas()
prepCds.defineSegments()



cds2Path = os.path.join(here, "chromosome1HomoSapien/CDS2.fasta")

cds2 = list()

try:
    with open(cds2Path, "r") as file:
        seq = []
        header = ''
        for line in file:
            if not line.startswith(">"):
                seq.append(line.strip())
            else:
                header = line.strip().replace(">", "")
                seq = []
            
        cds2 = [header,''.join(seq)]

except FileNotFoundError as e:
    print(e)
    exit(1)
except Exception as e:
    print(f"Erro inesperado: {e}")
    exit(1)

coo = [int(prepCds.coordenadas[0][1]), int(prepCds.coordenadas[0][0].replace('c', ''))]
segment = prepCds.complement[1][coo[0]:coo[1]]

if segment[::-1] in cds2[1]:
    print("sim")
else:
    print("nao")

