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
        # segmentos não codificantes
        self.finalSegments = list()


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
            if not self.complementar:
                start = 0
                
                for index in range(len(self.cds)):
                    end = int(self.cds[index][0]) - 2

                   
                    self.nonCds.append([start, end])
                    start = end 
                
                self.nonCds.append([start, self.length])
            else:
                start = -1

                for index in range(len(self.cds), 1, -1):
                    end = - int(self.cds[index -1][1])
                    
                    self.nonCds.append([start, end])
                    start = - int(self.cds[index - 1][0]) - 1
                
                self.nonCds.append([start, 0])
            
            print("testando defineNonCdsCoordinate")
            for index in range(len(self.nonCds) - 1):
                if self.complementar:
                    if self.nonCds[index][1] < self.nonCds[index + 1][0]:
                        print(index)
                        print("Coordenada na fita complementar inválida ")
                        exit(1)
                else:
                    if self.nonCds[index][1] > self.nonCds[index + 1][0]:
                        print(index)
                        print("Coordenada na fita normal inválida")
                        exit(1)
            print("Coordenadas verificadas com sucesso. function defineNonCdsCoordinate ok") 
            
            print(self.nonCds)
            print("Coordenadas das regiões não codificantes obtidas com sucesso")

            
            
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
    here = os.path.dirname(os.path.abspath(__file__))

    sequencePath = os.path.join(here, "chromosome1HomoSapien/sequence.fasta")
    complementPath = os.path.join(here, "chromosome1HomoSapien/reversedSequence.fasta")

    os.makedirs(os.path.join(here, "NonCds"), exist_ok=True)
    noCodingNoComplement = NonCoding(False)
    noCodingInComplement = NonCoding(True)



    print("Iniciando procedimento com a a fita no sentido normal")
    noCodingNoComplement.getSequence(sequencePath)
    noCodingNoComplement.getCoordenadas(os.path.join(here,"CDSsPreparados/cds.fasta"))
    
    noCodingNoComplement.defineNonCdsCoordinate()
    noCodingNoComplement.defineNonCds()
    print("Gravando os segmentos não codificantes da fita no sentido normal")
    noCodingNoComplement.write(os.path.join(here, "NonCds/nonCodingNoComplement.fasta"))
    print("procedimento com a a fita no sentido normal concluido")

    exit(1)

    print("Iniciando procedimento com a a fita no sentido complementar")
    noCodingInComplement.getSequence(complementPath)
    noCodingInComplement.getCoordenadas(os.path.join(here,"CDSsPreparados/cdsInComplement.fasta"))
    noCodingInComplement.defineNonCdsCoordinate()
    noCodingInComplement.defineNonCds()
    print("Gravando os segmentos não codificantes da fita no sentido complementar")
    noCodingInComplement.write(os.path.join(here, "NonCds/nonCodingInComplement.fasta"))
    print("procedimento com a a fita no sentido complementar concluido")

    end = time.time() - start
    print("Interação com o arquivo finalizado com sucesso")
    print(f"Tempo de execução: {end:.2f} segundos")









    
