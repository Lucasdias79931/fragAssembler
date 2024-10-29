import subprocess
import os
import time

# Classe Mafft
class Mafft:
    def __init__(self, reference_file, sequence_file, output_file) -> None:
        self.reference_file = reference_file
        self.sequence_file = sequence_file
        self.output_file = output_file

    def align(self):
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        command = ["mafft", "--add", self.sequence_file, self.reference_file]

        try:
            with open(self.output_file, "w") as file:
                subprocess.run(command, stdout=file, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o MAFFT: {e.stderr.decode('utf-8')}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

# Classe Minimap2
class Minimap2:
    def __init__(self, reference_file, sequence_file, output_file) -> None:
        self.reference_file = reference_file
        self.sequence_file = sequence_file
        self.output_file = output_file

    def align(self):
        command = [
            "minimap2",
            "-a",
            self.reference_file,
            self.sequence_file
        ]

        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        try:
            with open(self.output_file, "w") as out:
                subprocess.run(command, stdout=out, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o Minimap2: {e.stderr.decode('utf-8')}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

# Classe base Align usando polimorfismo
class Align:
    def __init__(self, aligner):
        self.aligner = aligner

    def perform_alignment(self):
        self.aligner.align()







