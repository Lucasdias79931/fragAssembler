import os
import re

class PrepareToAling:
    def __init__(self) -> None:
        # Dicionário para armazenar a sequência
        self.sequence = dict()
        # Lista para armazenar as coordenadas
        self.coordenadas = list()
        #posições validas:
        self.positions = list()
        #segmentos já tratados
        self.treatedSegments = list()
        #identifica se os segmentos são complementares
        self.complement = False

    def getSequence(self, directory: str) -> None:

        try:
            with open(directory, "r") as file:
                sequence_name = ""
                sequence = ""

               
                for line in file:
                    if not line.startswith('>'):  
                        sequence += line.strip() 
                        
                    else:
                        if sequence_name and sequence: 
                        
                            self.sequence[sequence_name] = sequence
                        sequence_name = line.strip().replace('>', '')  # Remove o '>'
                        sequence = ""  # Reseta a sequência

                # Adiciona a última sequência após o loop
                if sequence_name and sequence:
                    self.sequence[sequence_name] = sequence
            
            
            
        except FileNotFoundError as e:
            raise e
        except PermissionError as e:
            raise e
            
    def getCoordenadas(self) -> None:
        # Inicializa a lista de coordenadas
        coordenadas = []
    
        # Itera sobre os cabeçalhos do dicionário de sequências
        for header in self.sequence.keys():
            # Ajusta a regex para capturar as coordenadas
            padrao = r"([cC]?\d+)-(\d+)"
    
            # Usando re.findall para encontrar todas as correspondências
            resultados = re.findall(padrao, header)
    
            if resultados:
                # Adiciona as coordenadas encontradas na lista 'coordenadas'
                coordenadas.extend([list(resultado) for resultado in resultados])
    
        # Armazena as coordenadas no atributo da classe
        self.coordenadas = coordenadas

        if self.coordenadas[0][0].startswith("c"):
            self.complement = True
        print("Coordenadas obtidas com sucesso!")
    #define as posições corretas

    def definePosition(self):


        for i in range(len(self.coordenadas)):
            start = self.coordenadas[i][0]
            end = self.coordenadas[i][1]
            
            if start.startswith("c"):
                
                start  = start .replace("c","")
                
            
                
                # start - end pois está invertido a ordem da sequencia.
                coordenada = int(start) - int(end)
                self.positions.append(coordenada)
            else:

                
                
                coordenada = int(end) - int(start)
                self.positions.append(coordenada)
        
    # trata o segmento, caso seja um complemento de sequência
    
    
    # obtém os segmentos válidos para as sequências de acordo com as coordenadas
    def defineSegments(self):
        key = next(iter(self.sequence))
        sequence = self.sequence[key]

        
        start = 0

      
        
        for seq_len in self.positions:

            cds = ""
            end = start + seq_len
            
            
            for i in range(start, end):
                cds += sequence[i]

            
            self.treatedSegments.append(cds)
            start = end

    #preprara o cabeçalho para cada seguimento
    def prepareCab(self, nCoordenada):
        header = next(iter(self.sequence))
        print(header)
        
        # Expressão regular para extrair os elementos desejados
        pattern = r'^(.*?):.*?(H.*)$'

        # Busca os padrões na string
        match = re.search(pattern, header)
        
        header = list(match.groups())

        
        coordenada = f"{self.coordenadas[nCoordenada][0]}-{self.coordenadas[nCoordenada][1]}"

        print(f"{header[0]}:{coordenada} {header[1]}")
        return f"{header[0]}:{coordenada} {header[1]}"
        
    # escreve os CDSs nos arquivos.fasta 
    def write(self, directory):
        try:
            with open(directory, "a") as file:
                for nCoordenada in range(len(self.coordenadas)):
                    header = self.prepareCab(nCoordenada)
                    segment = self.treatedSegments[nCoordenada]
                    
                    file.write(f"{header}\n{segment}")
                    

        except FileExistsError as e:   
            print(e)    

           
        



###################### executar #####################

base_directory = os.getcwd()

for inter in range(2, 39):
    directory = os.path.join(base_directory, f"chromosome1HomoSapien/CDS{inter}.fasta")
    print(f"Preparando o arquivo: {directory}")
    prepare = PrepareToAling()
    prepare.getSequence(directory)
    prepare.getCoordenadas()
    prepare.definePosition()
    prepare.defineSegments()
    

   
    

  
    break
    
    
    
    
    

