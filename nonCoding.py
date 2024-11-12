import os
import re

class NonCoding:
    def __init__(self, complementar=None) -> None:
        # complementar ou não
        self.complementar = complementar
        # sequência para comparar
        self.sequence = list()
        # size of sequence
        self.length = 0
        # colhe as regiões codificantes
        self.cds = list()
        # Define as coordenadas das regiões não codificantes
        self.nonCds = list()


    # obter sequência

    def getSequence(self, directory: str) -> None:
        try:
            with open(directory, "r") as file:
                size = 0
                sequence = []
                header = "" 
                for line in file:
                    if not line.startswith(">"):
                        sequence.append(line.strip())
                        size += 1
                        
                    else:
                        header = line.strip().replace(">", "")
                        sequence = []
                if header and sequence:
                    self.length = size
                    self.sequence.extend([header, ''.join(sequence)])
        except FileNotFoundError as e:
            print(e)
            exit(1)
        except Exception as e:
            print(f"Erro inesperado: {e}")
            exit(1)
    
    def getCoordenadas(self, directory: str) -> None:

        try:
            with open(directory, "r") as file:
                
                for line in file:
                    if  line.startswith(">"):
                        padrao = r"([cC]?\d+)-(\d+)"
                        resultados = re.findall(padrao, line)

                        if len(resultados) > 0:

                            self.cds.append([resultados[0][0].replace("c", ""), resultados[0][1]])
                
        
            

        except FileNotFoundError as e:
            print(e)
            exit(1)
        except Exception as e:
            print(f"Erro inesperado: {e}")
            exit(1)

    def defineNonCds(self):
        if not self.complementar:
            start = 0

            for index in range(len(self.cds)):
                end = int(self.cds[index][0]) - 1

                self.nonCds.append([start, end])
                start = end + 1
            
            self.nonCds.append([start, self.length])
        else:
            start = self.length - 1

                







if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))

    sequencePath = os.path.join(here, "chromosome1HomoSapien/sequence.fasta")
    complementPath = os.path.join(here, "chromosome1HomoSapien/reversedSequence.fasta")

    test = NonCoding()
    test.getCoordenadas(os.path.join(here, "CDSsPreparadosC/cds1.fasta"))
    print(test.cds)
    
