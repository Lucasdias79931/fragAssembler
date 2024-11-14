import os
import re
import time

class PrepareCDSs:
    def __init__(self) -> None:
        #sequence 
        self.sequence = list()
        #complementar
        self.complement = list()
        # seguimentos 
        self.segmentsHeaders = list()
        # coordenadas
        self.coordenadas = list()
        # segmentos tratados
        self.finalSegments = list()
        

    def getSequence(self, directory: str, segment = False) -> None:

        try:
            with open(directory, "r") as file:
                header = ''
                sequence = []
                for line in file:
                    if not line.startswith(">"):
                        sequence.append(line.strip())
                    else:
                        if segment:
                            self.segmentsHeaders.append(line.strip().replace(">", ""))
                            break

                        header = line.strip().replace(">", "")
                        sequence = []

                if header and sequence:
                    return [header, ''.join(sequence)]
                        
                       
        except FileNotFoundError as e:
            print(e)
            exit(1)
            
    def getCoordenadas(self,) -> None:
        
        for header in self.segmentsHeaders:
            padrao = r"([cC]?\d+)-(\d+)"
            resultados = re.findall(padrao, header)
            if resultados:

                
                
                for i in range(len(resultados)):
                    
                        
                    coordenada = [resultados[i][0], resultados[i][1]]
            
                    self.coordenadas.append(coordenada)
        
        
    
    
    #preprara o cabeçalho para cada seguimento
    def prepareCab(self, coordenada):
        

        header = self.sequence[0]
        pattern = r'^(.*?) (.*)$'

        # Busca os padrões na string
        match = re.search(pattern, header)
        
        header = list(match.groups())

        
        
        

        return f">{header[0]}:{('-'.join(coordenada))} {header[1]}"

    
    # obtém os segmentos válidos para as sequências de acordo com as coordenadas
    def defineSegments(self):
        

        try:
            self.complement[1] = self.complement[1][::-1]

            for coordenada in self.coordenadas:
                if coordenada[0].startswith('c'):
                    seg = self.complement[1][int(coordenada[1]):int(coordenada[0].replace('c', ''))]
                    segment = [self.prepareCab(coordenada), seg[::-1]]
                    self.finalSegments.append(segment)
                else:
                    segment = [self.prepareCab(coordenada), self.sequence[1][int(coordenada[0]):int(coordenada[1])]]
                    self.finalSegments.append(segment)

        except Exception as e:
            print(f"Error:{e}")
            print("erro em defineSegments")
            exit(1)


    # escreve os CDSs nos arquivos.fasta 
    def write(self, cdsPath, cdsCPat):
        try:
            with open(cdsPath, "a") as file:
                with open(cdsCPat, "a") as fileC:
                    for segment in range(len(self.coordenadas)):
                        if self.coordenadas[segment][0].startswith('c'):
                            fileC.write(f"{self.finalSegments[segment][0]}\n{self.finalSegments[segment][1]}\n")
                        else:
                            file.write(f"{self.finalSegments[segment][0]}\n{self.finalSegments[segment][1]}\n")

            print("Inscrição realizada com sucesso!")

        
        except Exception as e:
            print(f"Error:{e}")
            print("erro em write")

           
        

 

###################### executar #####################
if __name__ == "__main__":
    start = time.time()
    here = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(here, "CDSsPreparados"), exist_ok=True)
    cdsDestinePath = os.path.join(here, "CDSsPreparados","cds.fasta")
    cdsCDestinePath = os.path.join(here, "CDSsPreparados","cdsInC.fasta")
    prepCds = PrepareCDSs()
    prepCds.sequence = prepCds.getSequence(os.path.join(here, "chromosome1HomoSapien/sequence.fasta"))
    prepCds.complement  = prepCds.getSequence(os.path.join(here, "chromosome1HomoSapien/reversedSequence.fasta"))

    for i in range(1, 39):
        prepCds.getSequence(os.path.join(here, f"chromosome1HomoSapien/CDS{i}.fasta"), True)
    
    prepCds.getCoordenadas()
    prepCds.defineSegments()    
    prepCds.write(cdsDestinePath, cdsCDestinePath)

    


    end = time.time() - start
    print(f"Fim da execução\nprocedimento realizado em {end:.4f} segundos!")

    
    
    
    
    
    

