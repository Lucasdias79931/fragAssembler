import os
import re

class PrepareToAling:
    def __init__(self) -> None:
        # Dicionário para armazenar a sequência
        self.sequence = dict()
        # Lista para armazenar as coordenadas
        self.coordenadas = list()
        # Aponta para quais coordenadas devo tratar
        self.coordenadasTotreat = list()
        #posições validas:
        self.positions = list()
        #segmentos já tratados
        self.treatedSegments = list()

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
    
        print("Coordenadas obtidas com sucesso!")
    #define as posições corretas

    def definePosition(self):

        cont = 0
        for i in self.coordenadas:
            coordenada = 0
            
            if i[0].startswith("c"):
                self.coordenadasTotreat.append(cont)
                i[0] = i[0].replace("c","")
            
            cont += 1
            coordenada = int(i[1]) - int(i[0])
            self.positions.append(coordenada)
        
    # trata o segmento, caso seja um complemento de sequência
    def treatComplement(self, segment: str) -> str:
        swap = {
            "A": "T",
            "T": "A",
            "G": "C",
            "C": "G"  
        }
        
        newseg = ""
        for i in segment:
            newseg += swap[i]  

        
        return newseg[::-1]  # Inverte a sequência complementar
    
    # obtém os segmentos válidos para as sequências de acordo com as coordenadas
    def defineSegments(self):
        key = next(iter(self.sequence))
        sequence = self.sequence[key]  
        start = 0

        # usa para verificar o index que aponta para o segmento que preciso tratar o complementar
        cont = 0
        
        for seq_len in self.positions:

            cds = ""
            end = start + seq_len
            
            
            for i in range(start, end):
                cds += sequence[i]

            if cont in self.coordenadasTotreat:
                
                cds = self.treatComplement(cds)
                

            cont += 1
            self.treatedSegments.append(cds)
            start = end

    

            
            
            

           
        



###################### executar #####################

base_directory = os.getcwd()

for inter in range(2, 39):
    directory = os.path.join(base_directory, f"chromosome1HomoSapien/CDS{inter}.fasta")
    print(f"Preparando o arquivo: {directory}")
    prepare = PrepareToAling()
    prepare.getSequence(directory)
    prepare.getCoordenadas()
    prepare.definePosition()
    
    """prepare.defineSegments()
    
    print(prepare.treatedSegments)"""
    break
    
    
    
    
    

