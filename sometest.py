import os 

base_directory = os.getcwd()
sequence = os.path.join(base_directory, "hromosome1HomoSapien/sequence.fasta")

lista = list()

try:
    if os.path.getsize(sequence) == 0:
        print("O arquivo está vazio.")
    else:
        with open(sequence, "r") as file:
            for line in file:
                if not line.startswith(">"):
                    break
                else:
            
                    lista.append(line)

except FileNotFoundError as e:
    print(f"Erro: {e}")
except PermissionError as e:
    print(f"Erro de permissão: {e}")

finally:
    print("Interação com o arquivo finalizado")

if lista:  # Verifica se a lista não está vazia
    print(lista[0])  # Imprime a primeira sequência
else:
    print("Nenhuma sequência válida encontrada.")
