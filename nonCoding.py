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
        #cabecalhos das regioes codificantes
        self.codingHeaders = list()
        #Regiões ncodificantes
        self.nocoding = list()
        self.sequencesNocoding = list()
        
       
        

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
                        header = line.strip().replace(">", "")
                        
                        self.codingHeaders.append(header)
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

    # sequences ncodificantes
    def defineSequencesNocoding(self):
        for i in range(len(self.nocoding)):
            start = self.nocoding[i][0]
            end = self.nocoding[i][1]
            self.sequencesNocoding.append(self.sequence[start:end])

    #prepara o cabecalho da regiao não codificante
    def prepareCab(self, nCoordenada, headerOri):
        header = headerOri
        
        
        # Expressão regular para extrair os elementos desejados
        pattern = r'^(.*?):.*?(H.*)$'

        # Busca os padrões na string
        match = re.search(pattern, header)
        
        header = list(match.groups())
        
        
        
        
        
       
        return f">{header[0]}:{self.nocoding[nCoordenada][0]}-{self.nocoding[nCoordenada][1]} {header[1]}"
        
            

    



################# executar ############################
if __name__ == "__main__":
    nonCoding = NonCoding()
    nonCodingToComplement  = NonCoding()

    
    here = os.path.dirname(os.path.abspath(__file__))

    
    nonCoding.get_sequence(os.path.join(here, f"chromosome1HomoSapien/sequence.fasta"))
    for CDS in range(1, 27):
        nonCoding.getCodingPositions(os.path.join(here, f"CDSsPreparadosParaAlinhar/CDS{CDS}.fasta"))

    nonCoding.defineNonCodingPositions()
    nonCoding.defineSequencesNocoding()

    for i in range(len(nonCoding.nocoding)):
        print(nonCoding.prepareCab(i, nonCoding.codingHeaders[i]))
        print(nonCoding.sequencesNocoding[i])
    
    nonCodingToComplement.get_sequence(os.path.join(here, f"chromosome1HomoSapien/genomeReverse.fasta"))

    for CDS in range(1, 13):
        nonCodingToComplement.getCodingPositions(os.path.join(here, f"CDSsComplementarPreparadosParaAlinhar/CDS{CDS}.fasta"))

    nonCodingToComplement.defineNonCodingPositions()
    nonCodingToComplement.defineSequencesNocoding()

    for i in range(len(nonCodingToComplement.nocoding)):
        print(nonCodingToComplement.prepareCab(i, nonCodingToComplement.codingHeaders[i]))
        print(nonCodingToComplement.sequencesNocoding[i])
        


    
    
    
    

            
        