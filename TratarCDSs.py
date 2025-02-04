from biopython import SeqIO
import os
import re
import time


class TratarCDSs:
    def __init__(self) -> None:
        # header and segment
        self.sequences = list()

        

    def getSequence(self, inputFile: str) -> None:
        try:
            with open(inputFile, "r") as handle:
                for header, sequence in SeqIO.parse(handle, "fasta"):
                    self.sequences.append([header, sequence])
        except FileNotFoundError as e:
            print(e)
            return None
        except IOError as e:
            print(e)
            return None
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return None
    

        
            
    
           
        

 


    
    
    
    
    

