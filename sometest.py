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

cds2 = ''

try:
    with open(cds2Path, "r") as file:
        seq = []
        for line in file:
            if not line.startswith(">"):
                seq.append(line.strip())
            
        cds2 = ''.join(seq)

except FileNotFoundError as e:
    print(e)
    exit(1)
except Exception as e:
    print(f"Erro inesperado: {e}")
    exit(1)

if prepCds.finalSegments[0][1] in cds2:
    print("sim")
else:
    print("nao")

