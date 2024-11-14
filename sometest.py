import os
def getSeq(directory: str):
    
    with open(directory, "r") as file:
        sequenceName = ""
        sequence = []
        for line in file:
            if not line.startswith(">"):
                sequence.append(line)
            else:
                sequenceName = line.strip().replace('>', '')
                sequence = []
        if sequenceName and sequence:
            return [sequenceName, ''.join(sequence)]
        return None
    
#c611297-611112,c610750-609083,c608056-607955,c601577-601398,c586955-586839


here = os.path.dirname(os.path.abspath(__file__))
complement = os.path.join(here, "chromosome1HomoSapien/reversedSequence.fasta")
segments = os.path.join(here, "chromosome1HomoSapien/CDS2fasta")

test = "lucasdias"

start = -1
end = -5

fatia = test[end:start]
print(fatia)


start = -1

end = 586839 - 586955


current = segments[1][end:start]

exit(1)


if current in complement[1]:
    print("sim")

else:
    print("nao")

start = end + 1

end = 610750-609083

current = segments[1][start:end]

if current in complement[1]:
    print("sim")

else:
    print("nao")