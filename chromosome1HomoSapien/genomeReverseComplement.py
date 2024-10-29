import os
import time

def reversed(sequence: str)-> str:
    nucleotide = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    base = "ACGT"
    complementReverse = ""
    for n in sequence:
        if n in base:
            complementReverse += nucleotide[n]
        else:
            complementReverse += n

    return complementReverse[::-1]

def getSeq(directory: str)-> dict:
    
    with open(directory, "r") as file:
        sequenceName = ""
        sequence = ""
        for line in file:
            if not line.startswith(">"):
                sequence += line.strip()
            else:
                sequenceName = line.strip().replace('>', '')
                sequence = ""
        if sequenceName and sequence:
            return [sequenceName, sequence]
        return None

################################ executar ############################
start = time.time()
base_directory = os.getcwd()

genome = os.path.join(base_directory, "sequence.fasta")

sequence = getSeq(genome)
print("sequencia original: ", sequence[0])
print("seguindo para a reveção do complementar: ")
reversedSeque = reversed(sequence[1])

destine = os.path.join(base_directory, "reversedSequence.fasta")

try:
    with open(destine, "w") as file:
        print(f"Escrevendo no arquivo: reversedSequence.fasta")
        file.write(f">{sequence[0]}\n")
        file.write(f"{reversedSeque}\n")
    
except FileNotFoundError as e:
    print(f"Erro: {e}")
except PermissionError as e:
    print(f"Erro de permissão: {e}")
finally:
    end = time.time() - start
    print("Interação com o arquivo finalizado com sucesso")
    print(f"Tempo de execução: {end:.2f} segundos")