import os
import re
import time

class PrepareToAling:
    def __init__(self) -> None:
        # se está no complemento
        self.complement = None
        # seguimentos 
        self.segments = list()
        # tamanho da sequência
        self.length = 0
        # coordenadas
        self.coordenadas = list()
        # segmentos tratados
        self.finalSegments = list()
        

    def getSequence(self, directory: str) -> None:

        try:
            with open(directory, "r") as file:

                sequence = []
                for line in file:
                    if not line.startswith(">"):
                        sequence.append(line.strip())
                    else:
                        self.segments.append(line.strip().replace(">", ""))


                        
                self.segments.append(''.join(sequence))
                self.length = len(self.segments[1])

                
                       
        except FileNotFoundError as e:
            print(e)
            exit(1)
            
    def getCoordenadas(self) -> None:
        header = self.segments[0]
    
        padrao = r"([cC]?\d+)-(\d+)"
        resultados = re.findall(padrao, header)
        if resultados:
            if resultados[0][0].startswith("c"):
                    self.complement = True
            for i in range(len(resultados)):
                
                    
                coordenada = [resultados[i][0], resultados[i][1]]
        
                self.coordenadas.append(coordenada)
        
    
    #reversa o complemento
    
     #preprara o cabeçalho para cada seguimento
    def prepareCab(self, coordenada):
        

        header = self.segments[0]
        pattern = r'^(.*?):.*?(H.*)$'

        # Busca os padrões na string
        match = re.search(pattern, header)
        
        header = list(match.groups())

        
        
        

        return f">{header[0]}:{('-'.join(coordenada))} {header[1]}"

    
    # obtém os segmentos válidos para as sequências de acordo com as coordenadas
    def defineSegments(self):
       
        if self.complement:
            start = int(self.length) - 1

            for index in range(len(self.coordenadas), 0, -1):
                
                end =  int(self.coordenadas[index - 1][1] ) -int(self.coordenadas[index - 1][0].replace("c", "")) 
                segment = []

                
                for n in range(self.length - 1, start + end, -1):
                    segment.append(self.segments[1][n])
                
                start += end -1
                
                self.finalSegments.append([self.prepareCab(self.coordenadas[index - 1]) ,''.join(segment)])

            self.finalSegments.reverse()

        else:
            start = 0

            for index in range(len(self.coordenadas)):
                end = int(self.coordenadas[index][1]) - int(self.coordenadas[index][0])
                segment = []
                
                for n in range(start, start + end):
                    segment.append(self.segments[1][n])
                
                start += end + 1
                
                self.finalSegments.append([self.prepareCab(self.coordenadas[index]),''.join(segment)])
                    
  
   
        
    # escreve os CDSs nos arquivos.fasta 
    def write(self, directory):
        try:
            with open(directory, "a") as file:
                for nCoordenada in range(len(self.coordenadas)):
                    header = self.finalSegments[nCoordenada][0]
                    segment = self.finalSegments[nCoordenada][1]
                    
                    file.write(f"{header}\n{segment}\n")
            print("Inscrição realizada com sucesso!")

        except FileExistsError as e:   
            print(e)    

           
        



###################### executar #####################
if __name__ == "__main__":
    start = time.time()
    here = os.path.dirname(os.path.abspath(__file__))

    InComp = 1
    NoComp = 1

    os.makedirs(os.path.join(here, "CDSsPreparados"), exist_ok=True)

    for iter in range(1, 39):
        cds = PrepareToAling()
        cds.getSequence(os.path.join(here, f"chromosome1HomoSapien/CDS{iter}.fasta"))
        cds.getCoordenadas()
        cds.defineSegments()

        if cds.complement:
            cds.write(os.path.join(here, f"CDSsPreparados/cdsInComplement.fasta"))
            
        else:
            cds.write(os.path.join(here, f"CDSsPreparados/cds.fasta"))
           
   
    


    end = time.time() - start
    print(f"Fim da execução\nprocedimento realizado em {end:.4f} segundos!")

    
    
    
    
    
    

