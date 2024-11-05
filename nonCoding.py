import os
import re

class NonCoding:
    def __init__(self) -> None:
        #sequência completa
        self.sequence = ""
        #tamanho da sequência
        self.length = 0
        #Regiões codificantes
        self.codingPositions = list()
        #Regiões ncodificantes
        self.nocoding = list()
       
        

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

    # Busca a região codificante 
    def getCodingPositions(self, file_name):
        try:
            headers = []
            with open(file_name, "r") as file:
                for line in file:
                    if line.startswith(">"):
                        header = line.strip()
                        padrao = r"([cC]?\d+)-(\d+)"
                        resultados = re.findall(padrao, header)
                        
                        if resultados:
                            
                            if resultados[0][0].startswith("c"):
                                resultados[0] = (resultados[0][1], resultados[0][0].replace("c", ""))
                            headers.extend(resultados)
                        
            self.codingPositions.extend(headers)

        except FileExistsError as e:
            print("ER :" + str(e))
        except FileNotFoundError as e:
            print("Error:" + str(e))

    
    def defineNonCodingPositions(self):
        if not self.codingPositions:
            print("Nenhuma sequência codificante foi encontrada")
            return
        
        start = 0 
        
        for pos in range(len(self.codingPositions)):
            end = int(self.codingPositions[pos][0]) - 1

            self.nocoding.append((start, end))
            start = int(self.codingPositions[pos][1])

        self.nocoding.append((start, self.length))

    
        
            

    



################# executar ############################
if __name__ == "__main__":
    nonCoding = NonCoding()
    nonCoding.get_sequence("chromosome1HomoSapien/sequence.fasta")

    nonCoding.getCodingPositions("CDSsComplementarPreparadosParaAlinhar/cds2.fasta")

    nonCoding.getCodingPositions("CDSsComplementarPreparadosParaAlinhar/cds3.fasta")
    print(f"codingPositions:{nonCoding.codingPositions}")
    nonCoding.defineNonCodingPositions()
    print(f"nocoding:{nonCoding.nocoding}")
    

            
        