import os
import re
import time
class NonCoding:
    def __init__(self) -> None:
        #sequência na fita normal
        self.sequence = list()
        #sequência na fita complementar
        self.complement = list()
        #coordenadas dos cds na fita normal
        self.CDSsCoordenadas = list()
        #coordenadas dos cds na fita complementar
        self.complementsCDSsCoordenadas = list()

        #coordenadas dos segmentos não codificantes na fita normal
        self.nonCodings  = list()
        #coordenadas dos segmentos não codificantes na fita complementar
        self.complementsNonCodings  = list()


        






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

    # Obter as coordenadas dos CDSs
    def getCoordenatesCDSs(self, directory: str) -> None:
        try:
            with open(directory, "r") as file:
                cds = []
                for line in file:
                    if line.startswith(">"):
                        padrao = r"([cC]?\d+)-(\d+)"
                        resultados = re.findall(padrao, line)

                        if len(resultados) > 0:

                            cds.append([resultados[0][0], resultados[0][1]])
            
            return cds
        except FileNotFoundError as e:
            print(e)
            exit(1)
        except Exception as e:
            print(f"Erro inesperado: {e}")
            exit(1)
    

   

    def defineNonCdsCoordinate(self, complement = False):
        

        try:
            if not complement:
                length = len(self.sequence[1])
                array = ['-'] * length
 
                                                                            
                

                for coordenada in self.CDSsCoordenadas:
                    
                    array[int(coordenada[0]):int(coordenada[1])] = self.sequence[1][int(coordenada[0]):int(coordenada[1])]
                
                
                start = 0
                started = True
                for n in range(len(array) -1):
                    if array[n] == "-":
                        end = n

                    if array[n +  1] != "-":
                        started = True

                    if array[n + 1] != "-" and started:
                        self.nonCodings.append([start, end])
                        
                        start = n + 1
                        started = False
                end = len(array) - 1
                self.nonCodings.append([start, end])

            else:
                length = len(self.sequence[1])
                array = ['-'] * length
 
                                                                            
                
                segment = self.complement[1][::-1]
                for coordenada in self.CDSsCoordenadas:
                    
                    array[int(coordenada[1]):int(coordenada[0].replace('c', ''))] = segment[int(coordenada[1]):int(coordenada[0].replace('c', ''))]
                
                
                start = 0
                started = True
                for n in range(len(array) -1):
                    if array[n] == "-":
                        end = n

                    if array[n +  1] != "-":
                        started = True

                    if array[n + 1] != "-" and started:
                        self.complementsNonCodings.append([end,start])
                        
                        start = n + 1
                        started = False
                end = len(array) - 1
                self.complementsNonCodings.append([end,start])
                self.complementsNonCodings = self.complementsNonCodings[::-1]
                
                
                
               
            
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

    print("colhendo coordeanadas dos CDSs na fita normal")
    nonCoding.CDSsCoordenadas = nonCoding.getCoordenatesCDSs(CDSsPath)
    print("coordenadas dos CDSs obtidos com sucesso")
    print("colhendo coordeanadas dos CDSs na fita complementar")
    nonCoding.complementsCDSsCoordenadas = nonCoding.getCoordenatesCDSs(CDSsComplementPath)
    print("coordenadas dos CDSs na fita complementar obtidos com sucesso")

    nonCoding.defineNonCdsCoordinate()
    nonCoding.defineNonCdsCoordinate(complement = True)

    print(nonCoding.nonCodings[0], nonCoding.nonCodings[len(nonCoding.nonCodings) - 1])
    print(nonCoding.complementsNonCodings[0], nonCoding.complementsNonCodings[len(nonCoding.complementsNonCodings) - 1])
    


    end = time.time() - start
    print("Interação com o arquivo finalizado com sucesso")
    print(f"Tempo de execução: {end:.2f} segundos")









    
