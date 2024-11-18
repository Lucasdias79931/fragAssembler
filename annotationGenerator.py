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
                        
                        self.annotations.append(line.strip())
            print("Annotations obitidas com sucesso")
        except FileNotFoundError as e:
            print(f"Error:{e}")
        

    def writeAnn(self, destine):
        try:
           
            with open(destine, "w") as file:
                for ann in self.annotations:
                    file.write(f"{ann}\n")
            print(f"Anotações escritas no diretorio:{destine}")
        except FileNotFoundError as e:
            print(f"Error:{e}")
        
    def clear_Ann(self):
        self.annotations.clear()



############### execução ########################

if __name__ == "__main__":
    
    here = os.path.dirname(os.path.abspath(__file__))
    Annotation = annotation()

    try:
       
       

        referenceSequence = os.path.join(here, "chromosome1HomoSapien/sequence.fasta")
        referenceSequenceReversed = os.path.join(here, "chromosome1HomoSapien/reversedSequence.fasta")
        cds = os.path.join(here, "CDSsPreparados/cds.fasta")
        cdsInC = os.path.join(here, "CDSsPreparados/cdsInC.fasta")
        nonCoding = os.path.join(here, "NonCds/nonCds.fasta")
        nonCodingInC = os.path.join(here, "NonCds/nonCdsInC.fasta")

        

        destineSequence = os.path.join(here, "Anotacoes/sequenceAnn.fasta")
        destineSequenceReversed = os.path.join(here, "Anotacoes/reversedSequenceAnn.fasta")
        destineCds = os.path.join(here, "Anotacoes/cdsAnn.fasta")
        destineCdsInC = os.path.join(here, "Anotacoes/cdsInCAnn.fasta")
        destineNonCds = os.path.join(here, "Anotacoes/nonCdsAnn.fasta")
        destineNonCdsInC = os.path.join(here, "Anotacoes/nonCdsInCAnn.fasta")
        

        os.makedirs(os.path.join(here, "Anotacoes"), exist_ok=True)
        
        Annotation.getAnn(referenceSequence)
        Annotation.writeAnn(destineSequence)
        Annotation.clear_Ann()

        Annotation.getAnn(referenceSequenceReversed)
        Annotation.writeAnn(destineSequenceReversed)
        Annotation.clear_Ann()

        Annotation.getAnn(cds)
        Annotation.writeAnn(destineCds)
        Annotation.clear_Ann()

        Annotation.getAnn(cdsInC)
        Annotation.writeAnn(destineCdsInC)
        Annotation.clear_Ann()

        Annotation.getAnn(nonCoding)
        Annotation.writeAnn(destineNonCds)
        Annotation.clear_Ann()

        Annotation.getAnn(nonCodingInC)
        Annotation.writeAnn(destineNonCdsInC)
        Annotation.clear_Ann()
    
    except SystemError as e:
            print(e)
        
        
   

    
    
    
    
    
        


    
