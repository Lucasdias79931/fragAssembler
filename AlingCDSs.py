from Aling import Align, Minimap2
import time
import os


base_directory = os.getcwd()

# Alinhar com Minimap2
start_timeWithMinimap2 = time.time()
for i in range(1, 27):
    reference_fasta = os.path.join(base_directory, f"chromosome1HomoSapien/sequence.fasta")
    fragments_fasta = os.path.join(base_directory, f"CDSsPreparados/cds{i}.fasta")
    seqs_alinhadas = os.path.join(base_directory, f"CDSsSemComplementosAlinhados{i}.sam")

    aligner = Minimap2(reference_fasta, fragments_fasta, seqs_alinhadas)
    align = Align(aligner)
    align.perform_alignment()

elapsed_timeWithMinimap2  = time.time() - start_timeWithMinimap2 