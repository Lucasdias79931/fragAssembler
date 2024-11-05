import os
import re

class NonCoding:
    def __init__(self) -> None:
        self.sequence = ""
        self.length = 0
        self.codingPositions= list()
    

    # obtém a sequência completa
    def get_sequence(self, genome_name):
        try:
            with open(genome_name, "r") as file:
                sequence = []
                for line in file:
                    if not line.startswith('>'):
                        sequence.append(line.strip())
                self.sequence = ''.join(sequence)
                self.length = len(self.sequence)
        except FileNotFoundError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

################# executar ############################
if __name__ == "__main__":
    nonCoding = NonCoding()
    nonCoding.get_sequence("chromosome1HomoSapien/sequence.fasta")

    print(f"length of sequence:{nonCoding.length}")

            
        