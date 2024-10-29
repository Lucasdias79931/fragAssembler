from Aling import Align, Minimap2
import time
import os


base_directory = os.getcwd()



# Alinhar com Minimap2
start_timeWithMinimap2 = time.time()
for i in range(1, 13):
    reference_fasta = os.path.join(base_directory, f"chromosome1HomoSapien/reversedSequence.fasta")
    fragments_fasta = os.path.join(base_directory, f"CDSsPreparadosC/cds{i}.fasta")
    seqs_alinhadas = os.path.join(base_directory, f"CDSsComComplementosAlinhados/cds{i}Alinhado.sam")

    aligner = Minimap2(reference_fasta, fragments_fasta, seqs_alinhadas)
    align = Align(aligner)
    align.perform_alignment()

elapsed_timeWithMinimap2  = time.time() - start_timeWithMinimap2 

print(f"Alinhamento realizado em {elapsed_timeWithMinimap2}s")