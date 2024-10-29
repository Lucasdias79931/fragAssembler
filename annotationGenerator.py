import os
import re

class annotation:
    def __init__(self):
        self.annotations = list()
    

    def getAnn(self, sequences):
        try:
            
            with open(sequences, "r") as file:
                for line in file:
                    if line.startswith(">"):
                        
                        self.annotations.append(re.split(r':| ', line))
            print("Annotations obitidas com sucesso")
        except FileNotFoundError as e:
            print(f"Error:{e}")
        

    def writeAnn(self, destine):
        try:
           
            with open(destine, "w") as file:
                for ann in self.annotations:
                    file.write(f"{ann[0]}\n")
            print(f"Anotações escritas no diretorio:{destine}")
        except FileNotFoundError as e:
            print(f"Error:{e}")
        
    def clear_Ann(self):
        self.annotations.clear()



############### execução ########################

if __name__ == "__main__":
    base_directory = os.getcwd()
    Annotation = annotation()

    try:
        for i in range(1, 12):
            
            CDSComplement = os.path.join(base_directory,f"CDSsComplementarPreparadosParaAlinhar/cds{i}.fasta")
            os.makedirs("Anotacoes/CDSsComplements/", exist_ok=True)
            destine = os.path.join(base_directory, f"Anotacoes/CDSsComplements/cds{i}.fasta")

            
            Annotation.getAnn(CDSComplement)
            Annotation.writeAnn(destine)
            Annotation.clear_Ann()
        print("CDSs complementares anotados com sucesso!\n")
    except SystemError as e:
            print(e)
        
        
    try:
        for i in range(1, 27):
            
            CDS = os.path.join(base_directory,f"CDSsPreparadosParaAlinhar/cds{i}.fasta")
            os.makedirs("Anotacoes/CDSs/", exist_ok=True)
            destine = os.path.join(base_directory, f"Anotacoes/CDSs/cds{i}.fasta")

            
            Annotation.getAnn(CDS)
            Annotation.writeAnn(destine)
            Annotation.clear_Ann()
        print("CDSs anotados com sucesso!\n")
    except SystemError as e:
            print(e)   
        
    try:
        print("Anotar sequência")
        sequence = os.path.join(base_directory,"chromosome1HomoSapien/sequence.fasta")
        os.makedirs("Anotacoes/chromosome/", exist_ok=True)
        destine = os.path.join(base_directory, f"Anotacoes/chromosome/sequence.fasta")

        Annotation.getAnn(sequence)
        Annotation.writeAnn(destine)
        Annotation.clear_Ann()

        print("Sequência anotada com suceso!\n")
    except SystemError as e:
            print(e)

    
    
    
    
    
        


    
