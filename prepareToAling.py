import os
import re

class PrepareToAling:
    def __init__(self) -> None:
        # Dicionário para armazenar a sequência
        self.sequence = dict()
        # Lista para armazenar as coordenadas
        self.coordenadas = list()

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
            print("Erro: "+ str(e))
            
        except PermissionError as e:
            print("Erro: "+ str(e))
            
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
        



###################### executar #####################

base_directory = os.getcwd()

for inter in range(1, 39):
    directory = os.path.join(base_directory, f"chromosome1HomoSapien/CDS{inter}.fasta")
    print(f"Preparando o arquivo: {directory}")
    prepare = PrepareToAling()
    prepare.getSequence(directory)
    prepare.getCoordenadas()
    print(prepare.coordenadas)
    
    
 