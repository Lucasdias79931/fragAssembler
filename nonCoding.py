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

        #sequência dos segmentos não codificantes na fita normal
        self.nonCodingsSequence = list()
        #sequência dos segmentos não codificantes na fita complementar
        self.complementsNonCodingsSequence = list()


        






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
                        padrao = r"(\d+)-([cC]?\d+)"
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
                    if not coordenada[0] == '0':
                        array[int(coordenada[0]) - 1:int(coordenada[1])] = self.sequence[1][int(coordenada[0]) - 1:int(coordenada[1])]
                        #necessario para não pegar indice negativo
                        
                    else:
                        array[int(coordenada[0]):int(coordenada[1])] = self.sequence[1][int(coordenada[0]):int(coordenada[1])]
                
                start = 0
                for n in range(len(array) -1):
                    if array[n] == "-":
                        end = n
                        if n == len(array) - 1:
                            self.nonCodings.append([f"{start}", f"{end}"])
                    else:
                        if array[n - 1] == "-":
                            self.nonCodings.append([f"{start}", f"{end}"])
                            
                        else:
                            start = n

                    

                   
               
                

            else:
                length = len(self.sequence[1])
                array = ['-'] * length
 
                                                                            
                

               
                for coordenada in self.complementsCDSsCoordenadas:
                    if not coordenada[0] == '0':
                        array[int(coordenada[0]) - 1:int(coordenada[1].replace('c', ''))] = self.complement[1][int(coordenada[0]) - 1:int(coordenada[1].replace('c', ''))]
                    else:
                        #nessario para não pegar indice negativo
                        array[int(coordenada[0]):int(coordenada[1].replace('c', ''))] = self.complement[1][int(coordenada[0]):int(coordenada[1].replace('c', ''))]

                
                start = 0
                for n in range(len(array) -1):
                    if array[n] == "-":
                        end = n
                        if n == len(array) - 1:
                            
                            self.complementsNonCodings.append([f"{start}", f"c{end}"])
                    else:
                        if array[n - 1] == "-":
                            
                            self.complementsNonCodings.append([f"{start}", f"c{end}"])
                          
                        else:
                            start = n
                        
                
                
                
                
               
            
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
            
                return f">{header[0]}:{'-'.join(coordenada)} {header[1]}"
            else:
                raise ValueError("Formato do cabeçalho inválido.")
        except Exception as e:
            print("erro em prepareCab")
            print(f"Erro inesperado: {e}")
            exit(1)

    # define os segmentos não codificantes
    def defineNonCds(self, complement = False):
        try:
            
        
            if not complement:
                
                
                for index in range(len(self.nonCodings)):
                    
                    if not self.nonCodings[index][0] == '0':

                        segment = self.sequence[1][int(self.nonCodings[index][0]) - 1 :int(self.nonCodings[index][1]) ]
                    else:
                        segment = self.sequence[1][int(self.nonCodings[index][0]) :int(self.nonCodings[index][1])]
                    header = self.prepareCab(self.nonCodings[index])
                    
                    if segment:
                        
                        
                        self.nonCodingsSequence.append([header, ''.join(segment)])
                    else:

                        
                        print(header, "nao adicionado")
                        print("Segmento vazio")
                    
            else:
                
                for index in range(len(self.complementsNonCodings )):
                    if not self.complementsNonCodings[index][0] == '0':
                        segment = self.complement[1][int(self.complementsNonCodings[index][0]) - 1:int(self.complementsNonCodings[index][1].replace('c', ''))]
                    else:
                        segment = self.complement[1][int(self.complementsNonCodings[index][0]):int(self.complementsNonCodings[index][1].replace('c', ''))]
                    
                    header = self.prepareCab(self.complementsNonCodings[index])
                    

                    if segment:
                        
                        
                        self.complementsNonCodingsSequence.append([header, ''.join(segment)])
                        
                    else:

                        
                        print(header, "nao adicionado")
                        print("Segmento vazio")
                        

        except Exception as e:
            print("erro em defineNonCds")
            print(f"Erro inesperado: {e}")
            exit(1)
    
    # escreve os segmentos
    def write(self, directory, complement = False):
        try:
            with open(directory, "w") as file:
                if not complement:
                    for segment in self.nonCodingsSequence:
                        
                        file.write(f"{segment[0]}\n{segment[1]}\n")
                else:
                    for segment in self.complementsNonCodingsSequence :
                        
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

    print("colhendo coordeanadas dos nonCds na fita normal")
    nonCoding.defineNonCdsCoordinate()
    print("coordenadas dos nonCds obtidos com sucesso")
    print("colhendo coordeanadas dos nonCds na fita complementar")
    nonCoding.defineNonCdsCoordinate(complement = True)
    print("coordenadas dos nonCds na fita complementar obtidos com sucesso")

    print("definindo os nonCds na fita normal")
    nonCoding.defineNonCds()
    print("nonCds na fita normal definidos com sucesso")
    print("definindo os nonCds na fita complementar")
    nonCoding.defineNonCds(complement = True)
    print("nonCds na fita complementar definidos com sucesso")

   
    os.makedirs(os.path.join(here, "NonCds"), exist_ok=True)
    nonCodingPath = os.path.join(here, "NonCds/nonCds.fasta")
    nonCodingComplementPath = os.path.join(here, "NonCds/nonCdsInC.fasta")

    #Escreve os nonCds na fita normal
    print("escrevendo os nonCds na fita normal")
    nonCoding.write(nonCodingPath)
    print("nonCds escritos com sucesso")
    #Escreve os nonCds na fita complementar
    print("escrevendo os nonCds na fita complementar")
    nonCoding.write(nonCodingComplementPath, True)
    print("nonCds escritos com sucesso")

    end = time.time() - start
    print("Interação com o arquivo finalizado com sucesso")
    print(f"Tempo de execução: {end:.2f} segundos")









    
