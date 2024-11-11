import os
import re
import time
class PrepareToAling:
    def __init__(self) -> None:
        # se está no complemento
        self.complement = None
        # seguimentos 
        self.segments = list()
        # coordenadas
        self.coordenadas = list()
        # posições corretas
        self.positions = list()
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

                
                       
        except FileNotFoundError as e:
            print(e)
            exit(1)
            
    def getCoordenadas(self) -> None:
        header = self.segments[0]
    
        padrao = r"([cC]?\d+)-(\d+)"
        resultados = re.findall(padrao, header)
        if resultados:
            for i in range(len(resultados)):
                if resultados[i][0].startswith("c"):
                    self.complement = True
                    coordenada = [resultados[i][1], resultados[i][0].replace("c", "")]
                    
                else:
                    coordenada = [resultados[i][0], resultados[i][1]]
        
                self.coordenadas.append(coordenada)
        
    
    #reversa o complemento
    def reversed(self, sequence: str)-> str:
        nucleotide = {
            "A": "T",
            "T": "A",
            "C": "G",
            "G": "C",
            
        }

        base = "ACGT"
        complementReverse = []
        for n in sequence:
            if n in base:
                complementReverse.append(nucleotide[n])
            else:
                complementReverse.append(n)

        return ''.join(complementReverse[::-1])
    
    #define as posições corretas
    def defineSegments(self):
        if self.complement:
            try:    
                self.segments[1] = self.reversed(self.segments[1])
                print("o segmento foi invertido!")
            except Exception as e:
                print(f"erro: {e}")


        
        for coordenadas in self.coordenadas:
            
            start = int(coordenadas[0])
            end = int(coordenadas[1])

            
            
                

    
    
    # obtém os segmentos válidos para as sequências de acordo com as coordenadas
    def defineSegments(self):
        
        for position in range(len(self.positions)):
            segment = 
    #preprara o cabeçalho para cada seguimento
    def prepareCab(self, nCoordenada):
        ...
        
    # escreve os CDSs nos arquivos.fasta 
    def write(self, directory):
        try:
            with open(directory, "w") as file:
                for nCoordenada in range(len(self.coordenadas)):
                    header = self.prepareCab(nCoordenada)
                    segment = self.treatedSegments[nCoordenada]
                    
                    file.write(f"{header}\n{segment}\n")
            print("Inscrição realizada com sucesso!")

        except FileExistsError as e:   
            print(e)    

           
        



###################### executar #####################
if __name__ == "__main__":
    start = time.time()
    here = os.path.dirname(os.path.abspath(__file__))

    test = PrepareToAling()
    test.getSequence(os.path.join(here, "chromosome1HomoSapien/CDS2.fasta"))
    test.getCoordenadas()
    
   
    


    end = time.time() - start
    print(f"Fim da execução\nprocedimento realizado em {end:.4f} segundos!")

    
    
    
    
    
    

