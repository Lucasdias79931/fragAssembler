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
        self.nocodingPositions = list()
        

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
    def getCodingPosition(self, file_name):
        try:
            headers = []
            with open(file_name, "r") as file:
                for line in file:
                    if line.startswith(">"):
                        header = line.strip()
                        
                        padrao = r"([cC]?\d+)-(\d+)"
    
                
                        resultados = re.findall(padrao, header)
                        headers.extend(resultados)
                    
            self.codingPositions.extend(headers)
        except FileExistsError as e:
            print("ER :" + e)
        except FileNotFoundError as e:
            print("Error:" + e)
    



################# executar ############################
if __name__ == "__main__":
    nonCoding = NonCoding()
    nonCoding.get_sequence("chromosome1HomoSapien/sequence.fasta")

    nonCoding.getCodingPosition("CDSsPreparadosParaAlinhar/cds2.fasta")

    nonCoding.getCodingPosition("CDSsPreparadosParaAlinhar/cds3.fasta")
    print(f"codingPositions:{nonCoding.codingPositions}")

            
        