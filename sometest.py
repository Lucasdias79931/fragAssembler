import os 

base_directory = os.getcwd()
sequence = os.path.join(base_directory, "chromosome1HomoSapien/CDS3.fasta")

lista = list()

try:
    if os.path.getsize(sequence) == 0:
        print("O arquivo está vazio.")
    else:
        with open(sequence, "r") as file:
            seq = ""
            for line in file:
                if not line.startswith(">"):
                    seq += line.strip()
                else:
            
                    lista.append(line.strip())
            lista.append(seq)

except FileNotFoundError as e:
    print(f"Erro: {e}")
except PermissionError as e:
    print(f"Erro de permissão: {e}")

finally:
    print("Interação com o arquivo finalizado")

"""if lista:  # Verifica se a lista não está vazia
    print(lista)  # Imprime a primeira sequência
else:
    print("Nenhuma sequência válida encontrada.")"""

## contar de dois em dois. coordenadas para o CDS2
coordenadas = (961342,961552,961629,961750,961826,962047,962286,962471,962704,962917,
               963109,963253,963337,963504,963920,964008,964107,964180,964349,964530,
               964963,965191)


newCO = []

for i in range(0, len(coordenadas), 2):
    newCO.append(coordenadas[i+1] - coordenadas[i])
    
    
print("coordenadas:", newCO)

newList = list()

start = 0  # Indica o ponto inicial na sequência de nucleotídeos
Ncoordenada = 0
for seq_len in newCO:  # 'seq_len' é o tamanho do fragmento entre as coordenadas
    cds = ""
    end = start + seq_len  # Calcula a coordenada final do fragmento
    for i in range(start, end):  # Itera de start até o ponto final
        cds += lista[1][i]  # Adiciona os nucleotídeos à sublista
    newList.append(cds)  # Adiciona a sublista à lista final
    start = end  # Atualiza o início para a próxima iteração
    
    Ncoordenada += 1
print(Ncoordenada)


