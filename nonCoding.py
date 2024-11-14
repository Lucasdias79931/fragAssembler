import os
import re
import time

class NonCoding:
    def __init__(self) -> None:
        #sequência na fita normal
        self.sequence = list()
        #sequência na fita complementar
        self.complement = list()
        #headers dos cds na fita normal
        self.CDSsHeaders = list()
        #headers dos cds na fita complementar
        self.complementsCDSsHeaders = list()
        #coordenadas dos cds na fita normal
        self.CDSsCoordenadas = list()
        #coordenadas dos cds na fita complementar
        self.complementsCDSsCoordenadas = list()
        






    # obter sequência e complemento da sequência

    def getSequence(self, directory: str):
        try:
            with open(directory, "r") as file:
                
                sequence = []
                header = "" 
                for line in file:
                    if not line.startswith(">"):
                        sequence.append(line.strip())
                        
                   
                    else:
                        header = line.strip().replace(">", "")
                        sequence = []

                if header and sequence:
                    return [header, ''.join(sequence)]
                
        except FileNotFoundError as e:
            print(e)
            exit(1)
        except Exception as e:
            print(f"Erro inesperado: {e}")
            exit(1)
    # Obter os cds
    def getCDSs(self, directory: str) -> None:
        try:
            with open(directory, "r") as file:
                cds = []
                for line in file:
                    if line.startswith(">"):
                        cds.append(line.strip())
            
            return cds
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

                            self.cds.append([int(resultados[0][0].replace("c", "")), int(resultados[0][1])])
    
        except FileNotFoundError as e:
            print(e)
            exit(1)
        except Exception as e:
            print(f"Erro inesperado: {e}")
            exit(1)

    #verifica se os cds estao ordenados
   

    def defineNonCdsCoordinate(self):
        

        try:
            ...

            
            
        except Exception as e:
            print(f"Erro inesperado: {e}")
            exit(1)
        
    # prepara o cabeçalho de cada segmento
    def prepareCab(self, coordenada):
        try:
            header = self.sequence[0]
            pattern = r'^(.*?) (.*)$'
            match = re.search(pattern, header)

            if match:
                header = list(match.groups())
                
                if self.complementar:
                    coordenada[0] = 'c' + str(coordenada[0])

                # Converte os elementos de coordenada para strings antes de usar join
                coordenada_str = list(map(str, coordenada))
                return f">{header[0]}:{('-'.join(coordenada_str))} {header[1]}"
            else:
                raise ValueError("Formato do cabeçalho inválido.")
        except Exception as e:
            print("erro em prepareCab")
            print(f"Erro inesperado: {e}")
            exit(1)


    def defineNonCds(self):
        try:
            
        
            if not self.complementar:
                print("testando defineNonCds notComplement")
                for index in range(len(self.nonCds) - 1):
                    
                    if self.nonCds[index][1] < self.nonCds[index + 1][0]:
                        print(index)
                        print("Coordenada na fita complementar inválida ")
                        exit(1)
                print("Coordenadas verificadas com sucesso. function defineNonCds ok")
                exit(1)
                
                for index in range(len(self.nonCds)):
                    segment = self.sequence[1][int(self.nonCds[index][0]):int(self.nonCds[index][1])]
                    
                    header = self.prepareCab(self.nonCds[index])
                    
                    if segment:
                        print(header, "adicionado")
                        
                        self.finalSegments.append([header, ''.join(segment)])
                    else:

                        
                        print(header, "nao adicionado")
                        print("Segmento vazio")
                    
            else:
                for index in self.nonCds:

                    segment = self.sequence[1][index[1]:index[0]]
                    header = self.prepareCab(index)
                    
                    if segment:
                        self.finalSegments.append([header, ''.join(segment)])
                    else:
                        print("Segmento vazio")
                        

        except Exception as e:
            print("erro em defineNonCds")
            print(f"Erro inesperado: {e}")
            exit(1)
    
    # escreve os segmentos
    def write(self, directory):
        try:
            with open(directory, "w") as file:
                for segment in self.finalSegments:
                    
                    file.write(f"{segment[0]}\n{segment[1]}\n")
            print("Inscrição realizada com sucesso!")

        except FileExistsError as e:   
            print(e)    








if __name__ == "__main__":
    start = time.time()
    print("Iniciando o processo para extrair os nonCds")
    here = os.path.dirname(os.path.abspath(__file__))
    
    sequencePath = os.path.join(here, "chromosome1HomoSapien/sequence.fasta")
    complementPath = os.path.join(here, "chromosome1HomoSapien/reversedSequence.fasta")
    CDSsPath = os.path.join(here, "CDSsPreparados/cds.fasta")
    CDSsComplementPath = os.path.join(here, "CDSsPreparados/cdsInC.fasta")

    os.makedirs(os.path.join(here, "NonCds"), exist_ok=True)
    
    nonCoding = NonCoding()
    print("colhendo sequência na fita normal")
    nonCoding.sequence = nonCoding.getSequence(sequencePath)
    print("sequência obtida com sucesso")
    print("colhendo sequência na fita complementar")
    nonCoding.complement = nonCoding.getSequence(complementPath)
    print("sequência obtida com sucesso")

    print("colhendo CDSs na fita normal")
    nonCoding.CDSsHeaders = nonCoding.getCDSs(CDSsPath)
    print("CDSs obtidos com sucesso")
    print("colhendo CDSs na fita complementar")
    nonCoding.complementsCDSsHeaders = nonCoding.getCDSs(CDSsComplementPath)
    print("CDSs na fita complementar obtidos com sucesso")
    


    end = time.time() - start
    print("Interação com o arquivo finalizado com sucesso")
    print(f"Tempo de execução: {end:.2f} segundos")









    
