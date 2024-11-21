import os
import sys 



class Coding:
    def __init__(self):
        self.segments = list()
        self.segmentsInComplement = list()
        self.frames = list()
        self.tableCodons = {
        "GCT": "A",  # Alanina
        "GCC": "A",  # Alanina
        "GCA": "A",  # Alanina
        "GCG": "A",  # Alanina
        "TGT": "C",  # Cisteína
        "TGC": "C",  # Cisteína
        "GAT": "D",  # Ácido aspártico
        "GAC": "D",  # Ácido aspártico
        "GAA": "E",  # Ácido glutâmico
        "GAG": "E",  # Ácido glutâmico
        "TTT": "F",  # Fenilalanina
        "TTC": "F",  # Fenilalanina
        "GGT": "G",  # Glicina
        "GGC": "G",  # Glicina
        "GGA": "G",  # Glicina
        "GGG": "G",  # Glicina
        "CAT": "H",  # Histidina
        "CAC": "H",  # Histidina
        "ATT": "I",  # Isoleucina
        "ATC": "I",  # Isoleucina
        "ATA": "I",  # Isoleucina
        "TTA": "L",  # Leucina
        "TTG": "L",  # Leucina
        "CTT": "L",  # Leucina
        "CTC": "L",  # Leucina
        "CTA": "L",  # Leucina
        "CTG": "L",  # Leucina
        "AAA": "K",  # Lisina
        "AAG": "K",  # Lisina
        "ATG": "M",  # Metionina
        "AAT": "N",  # Asparagina
        "AAC": "N",  # Asparagina
        "CCT": "P",  # Prolina
        "CCC": "P",  # Prolina
        "CCA": "P",  # Prolina
        "CCG": "P",  # Prolina
        "CAA": "Q",  # Glutamina
        "CAG": "Q",  # Glutamina
        "CGT": "R",  # Arginina
        "CGC": "R",  # Arginina
        "CGA": "R",  # Arginina
        "CGG": "R",  # Arginina
        "AGA": "R",  # Arginina
        "AGG": "R",  # Arginina
        "TCT": "S",  # Serina
        "TCC": "S",  # Serina
        "TCA": "S",  # Serina
        "TCG": "S",  # Serina
        "AGT": "S",  # Serina
        "AGC": "S",  # Serina
        "ACT": "T",  # Treonina
        "ACC": "T",  # Treonina
        "ACA": "T",  # Treonina
        "ACG": "T",  # Treonina
        "GTT": "V",  # Valina
        "GTC": "V",  # Valina
        "GTA": "V",  # Valina
        "GTG": "V",  # Valina
        "TGG": "W",  # Triptofano
        "TAT": "Y",  # Tirosina
        "TAC": "Y",  # Tirosina
        "TAA": "Stop",  # Stop
        "TAG": "Stop",  # Stop
        "TGA": "Stop",  # Stop
    }

    def getSequence(self, directory: str, complement = False) -> None:
        try:
            with open(directory, "r") as file:
                allSec = []
                sequence = []
                header = "" 
                for line in file:
                    if not line.startswith(">"):
                        sequence.append(line.strip())
                        
                   
                    else:
                        header = line.strip().replace(">", "")
                        sequence = []

                    if header and sequence:
                        allSec.append([header, ''.join(sequence)])
                        header = ""
                        sequence = []
                
                if complement:
                    self.segmentsInComplement.extend(allSec)
                else:
                    self.segments.extend(allSec)
        except FileNotFoundError as e:
            print(e)
            exit(1)
        except Exception as e:
            print(f"Erro inesperado: {e}")
            exit(1)
    
    def traduction(self, sequence: str) -> str:
        try:
            translated = ""
        
            for i in range(0, len(sequence), 3):
                
                codon = sequence[i:i+3]

                if len(codon) < 3:
                    break

                amino = self.tableCodons.get(codon, "Error")

                if amino == "Stop":
                    translated += f"* (parada) códon: {codon}-"
                    #break
                else:
                    translated += amino + "-"
            return translated
        except Exception as e:
            print(f"Erro inesperado: {e}")
            exit(1)
    
    def complementR(self, sequence: str) -> str:
       

        nuc = { "A": "T", "T": "A", "C": "G", "G": "C" }

        
        complement = [nuc[n] for n in sequence]
       

        return "".join(complement[::-1])

    

######################################### executar #########################################

if __name__ == "__main__":
    coding = Coding()
    print("Carregando CDSs na fita normal...")
    coding.getSequence("CDSsPreparados/cds.fasta")
    print("CDSs carregados com sucesso!")

    print("Carregando CDSs na fita complementar...")
    coding.getSequence("CDSsPreparados/cdsInC.fasta", True)
    print("CDSs carregados com sucesso!")

    os.makedirs("CDSsTraduzidos", exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))

    CDSsTraduzidosPath = os.path.join(here, "CDSsTraduzidos/cdsTraduzidos.fasta")
    CDSsTraduzidosPathComplement = os.path.join(here, "CDSsTraduzidos/cdsInCTraduzidos.fasta")

    try:
        with open(CDSsTraduzidosPath, "w") as file:
            for segment in coding.segments:
                
                file.write(segment[0] + "\n\n")

                for i in range(3):

                    file.write(f"Frame +{i+ 1} (Sentido direto):\n")

                    sequenceTrans = coding.traduction(segment[1][i:])
                    file.write(f"\nTradução: {sequenceTrans}\n\n")

                for i in range(3):

                    file.write(f"Frame +{i+ 1} (Sentido complementar reverso):\n")
                    segment[1] = coding.complementR(segment[1])
                    sequenceTrans = coding.traduction(segment[1][i:])
                    file.write(f"\nTradução: {sequenceTrans}\n\n")
                
    except FileNotFoundError as e:
        print(f"Error:{e}")
        exit(1)
    except Exception as e:
        print(f"Error:{e}")
        exit(1)
    
    try:
        with open(CDSsTraduzidosPathComplement, "w") as file:
            for segment in coding.segmentsInComplement:
                
                file.write(segment[0] + "\n\n")

                for i in range(3):

                    file.write(f"Frame +{i+ 1} (Sentido complementar reverso):\n")

                    sequenceTrans = coding.traduction(segment[1][i:])
                    file.write(f"\nTradução: {sequenceTrans}\n\n")

                for i in range(3):

                    file.write(f"Frame +{i+ 1} (Sentido direto):\n")
                    segment[1] = coding.complementR(segment[1])
                    sequenceTrans = coding.traduction(segment[1][i:])
                    file.write(f"\nTradução: {sequenceTrans}\n\n")
                
    except FileNotFoundError as e:
        print(f"Error:{e}")
        exit(1)
    except Exception as e:
        print(f"Error:{e}")
        exit(1)
    
