import os
import re
import time

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
                    #print("Sequência obtida com sucesso")
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
                
        
            print("Coordenadas das regiões codificantes obtidas com sucesso")

        except FileNotFoundError as e:
            print(e)
            exit(1)
        except Exception as e:
            print(f"Erro inesperado: {e}")
            exit(1)

    #verifica se os cds estao ordenados
    def ordenado(self):
        if not self.complementar:
            for inter in range(len(self.cds) - 1):
                if int(self.cds[inter][1]) > int(self.cds[inter + 1][1]):
                    self.cds[inter], self.cds[inter + 1] = self.cds[inter + 1], self.cds[inter]
            
        else:
            for inter in range(len(self.cds) - 1):
                if int(self.cds[inter][1]) < int(self.cds[inter + 1][1]):
                    self.cds[inter], self.cds[inter + 1] = self.cds[inter + 1], self.cds[inter]

    def defineNonCds(self):
        self.ordenado()

        try:
            if not self.complementar:
                start = 0

                for index in range(len(self.cds)):
                    end = int(self.cds[index][0]) - 1

                    self.nonCds.append([start, end])
                    start = end + 1
                
                self.nonCds.append([start, self.length])
            else:
                start = self.length - 1

                for index in range(len(self.cds)):
                    end = int(self.cds[index][1]) - 1

                    self.nonCds.append([start, end])
                    start = end - 1
                
                self.nonCds.append([start, -1])
            print("Coordenadas das regiões não codificantes obtidas com sucesso")

        except Exception as e:
            print(f"Erro inesperado: {e}")
            exit(1)
        
    # prepara o cabeçalho de cada segmento
    def prepareCab(self, coordenada):

        header = self.sequence[0]
        pattern = r'^(.*?):.*?(H.*)$'

        # Busca os padrões na string
        match = re.search(pattern, header)
        
        header = list(match.groups())

        
        if self.complementar:
            aux = 'c'
            aux += coordenada[0]
            coordenada[0] = aux
        

        return f">{header[0]}:{('-'.join(coordenada))} {header[1]}"


                







if __name__ == "__main__":
    start = time.time()
    here = os.path.dirname(os.path.abspath(__file__))

    sequencePath = os.path.join(here, "chromosome1HomoSapien/sequence.fasta")
    complementPath = os.path.join(here, "chromosome1HomoSapien/reversedSequence.fasta")

    
    noCodingNoComplement = NonCoding(False)
    noCodingInComplement = NonCoding(True)



    print("Iniciando procedimento com a a fita no sentido normal")
    noCodingNoComplement.getSequence(sequencePath)
    noCodingNoComplement.getCoordenadas(os.path.join(here,"CDSsPreparados/cds.fasta"))
    noCodingNoComplement.defineNonCds()












    
