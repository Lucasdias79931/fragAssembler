import subprocess
import time
import os

class Minimap2:
    def __init__(self) -> None:
        pass

    @staticmethod
    def align(reference_file, sequence_file, output_file):
        command = [
            "minimap2",
            "-a",
            reference_file,
            sequence_file
        ]

        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        try:
            with open(output_file, "w") as out:
                subprocess.run(command, stdout=out, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o Minimap2: {e.stderr.decode('utf-8')}")
        except Exception as e:
            print(f"Erro inesperado: {e}")


########################### executar ############################
here = os.path.dirname(os.path.abspath(__file__))



# Alinhar com Minimap2
start_timeWithMinimap2 = time.time()

referenceSequence = os.path.join(here, "chromosome1HomoSapien/sequence.fasta")
referenceSequenceReversed = os.path.join(here, "chromosome1HomoSapien/reversedSequence.fasta")
cds = os.path.join(here, "CDSsPreparados/cds.fasta")
cdsInC = os.path.join(here, "CDSsPreparados/cdsInC.fasta")
nonCoding = os.path.join(here, "NonCds/nonCds.fasta")
nonCodingInC = os.path.join(here, "NonCds/nonCdsInC.fasta")

os.makedirs(os.path.join(here, "Alinhados"), exist_ok=True)

destineCds = os.path.join(here, "Alinhados/cdsAling.fasta")
destineCdsInC = os.path.join(here, "Alinhados/cdsInCAling.fasta")
destineNonCds = os.path.join(here, "Alinhados/nonCdsAling.fasta")
destineNonCdsInC = os.path.join(here, "Alinhados/nonCdsInCAling.fasta")

Minimap2.align(referenceSequence, cds, destineCds)
Minimap2.align(referenceSequenceReversed, cdsInC, destineCdsInC)
Minimap2.align(referenceSequence, nonCoding, destineNonCds)
Minimap2.align(referenceSequenceReversed, nonCodingInC, destineNonCdsInC)



elapsed_timeWithMinimap2  = time.time() - start_timeWithMinimap2 

print(f"Alinhamento realizado em {elapsed_timeWithMinimap2}s")