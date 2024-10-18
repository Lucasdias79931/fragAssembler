import os

class PrepareToAling:
    def __init__(self) -> None:
        self.sequence = dict()

    def getSequence(self, directory: str) -> None:

        try:
            with open(directory, "r") as file:
                header = ""
                seq = ""
                for line in file:
                    if not line.startswith(">"):
                        seq += line.split("\n")[0]
                    else:
                        header = line

                if header and seq:
                    self.sequence[header] = seq
            
        except FileNotFoundError as e:
            print("Erro: "+ str(e))
            return None
        except PermissionError as e:
            print("Erro: "+ str(e))
            return None



###################### executar #####################

base_directory = os.getcwd()

for inter in range(1, 39):
    directory = os.path.join(base_directory, f"chromosome1HomoSapien/CDS{inter}.fasta")
    print(f"Preparando o arquivo: {directory}")
    prepare = PrepareToAling()
    prepare.getSequence(directory)
    print(prepare.sequence)