import os
import re

class NonCoding:
    def __init__(self, complementar=None) -> None:
        # complementar ou não
        self.complementar = complementar
        # sequência completa
        self.sequence = ""
        # cabeçalho da sequência
        self.headerSec = ""
        # tamanho da sequência
        self.length = 0
        # Regiões codificantes
        self.codingPositions = list()
        # cabeçalhos das regiões codificantes
        self.codingHeaders = list()
        # Regiões não codificantes
        self.nocoding = list()
        # sequências não codificantes
        self.sequencesNocoding = list()
        # cabeçalhos das sequências
        self.newHeaders = list()

    # obtém a sequência completa
    def get_sequence(self, genome_name):
        try:
            with open(genome_name, "r") as file:
                sequence = []
                header = ""
                for line in file:
                    if not line.startswith('>'):
                        sequence.append(line.strip())
                    else:
                        header = line.strip()
                self.headerSec = header.strip().replace('>', '')
                self.sequence = ''.join(sequence)
                self.length = len(self.sequence)
        except FileNotFoundError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

    # Busca a região codificante
    def getCodingPositions(self, file_name):
        try:
            headers = []
            with open(file_name, "r") as file:
                for line in file:
                    if line.startswith(">"):
                        header = line.strip().replace(">", "")
                        self.codingHeaders.append(header)
                        padrao = r"([cC]?\d+)-(\d+)"
                        resultados = re.findall(padrao, header)
                        if resultados:
                            if resultados[0][0].startswith("c"):
                                resultados[0] = (resultados[0][1], resultados[0][0].replace("c", ""))
                            headers.extend(resultados)
            self.codingPositions.extend(headers)

        except FileExistsError as e:
            print("ER :" + str(e))
        except FileNotFoundError as e:
            print("Error:" + str(e))

    def defineNonCodingPositions(self):
        if not self.codingPositions:
            print("Nenhuma sequência codificante foi encontrada")
            return

        start = 0
        for pos in range(len(self.codingPositions)):
            if pos < len(self.codingPositions):
                end = int(self.codingPositions[pos][0]) - 1
                self.nocoding.append((start, end))
                start = int(self.codingPositions[pos][1])
        
        self.nocoding.append((start, self.length))

    # define as sequências não codificantes
    def defineSequencesNocoding(self):
        for i in range(len(self.nocoding)):
            start = self.nocoding[i][0]
            end = self.nocoding[i][1]
            self.sequencesNocoding.append(self.sequence[start:end])

    # prepara o cabeçalho da região não codificante
    def prepareCab(self, nCoordenada):
        header = self.headerSec
        pattern = r'^(NC_\d+\.\d+)\s+(.*)\s+(.*)$'
        match = re.search(pattern, header)
        
        if match and nCoordenada < len(self.codingPositions):
            header = list(match.groups())
            coordenada = f"{self.codingPositions[nCoordenada][0]}-{self.codingPositions[nCoordenada][1]}"
            header = f">{header[0]}:{coordenada} {header[1]} {header[2]} "
            self.newHeaders.append(header)
        else:
            print("Padrão não encontrado na string ou coordenada fora de alcance")

    def write(self, destine: str, header: str, sec: str):
        try:
            with open(destine, "a") as file:
                file.write(f"{header}\n")
                file.write(f"{sec}\n")
        except FileNotFoundError as e:
            print(f"Error:{e}")

if __name__ == "__main__":
    nonCoding = NonCoding()
    nonCodingToComplement = NonCoding(True)
    here = os.path.dirname(os.path.abspath(__file__))

    nonCoding.get_sequence(os.path.join(here, "chromosome1HomoSapien/sequence.fasta"))
    for CDS in range(1, 27):
        pathCDS = os.path.join(here, f"CDSsPreparadosParaAlinhar/cds{CDS}.fasta")
        nonCoding.getCodingPositions(pathCDS)

    nonCoding.defineNonCodingPositions()
    nonCoding.defineSequencesNocoding()

    for i in range(len(nonCoding.nocoding)):
        try:
            nonCoding.prepareCab(i)
        except Exception as e:
            print(f"Erro inesperado: {e}")
            print(len(nonCoding.nocoding))
            print(i)
            exit(1)

    nonCodingToComplement.get_sequence(os.path.join(here, "chromosome1HomoSapien/reversedSequence.fasta"))
    for CDS in range(1, 13):
        nonCodingToComplement.getCodingPositions(os.path.join(here, f"CDSsComplementarPreparadosParaAlinhar/cds{CDS}.fasta"))

    nonCodingToComplement.defineNonCodingPositions()
    nonCodingToComplement.defineSequencesNocoding()

    for i in range(len(nonCodingToComplement.nocoding)):
        nonCodingToComplement.prepareCab(i)

    destineNonCoding = os.path.join(here, "Regioes_nao_codificantes/_fita_comum")
    destineNonCodingInComplement = os.path.join(here, "Regioes_nao_codificantes/_fita_complementar")
    os.makedirs(destineNonCoding, exist_ok=True)
    os.makedirs(destineNonCodingInComplement, exist_ok=True)

    for sec in range(len(nonCoding.sequencesNocoding)):
        if sec < len(nonCoding.newHeaders):
            nonCoding.write(os.path.join(destineNonCoding, "fitaComum.fasta"), nonCoding.newHeaders[sec], nonCoding.sequencesNocoding[sec])

    for sec in range(len(nonCodingToComplement.sequencesNocoding)):
        if sec < len(nonCodingToComplement.newHeaders):
            nonCodingToComplement.write(os.path.join(destineNonCodingInComplement, "fitaComplementar.fasta"), nonCodingToComplement.newHeaders[sec], nonCodingToComplement.sequencesNocoding[sec])
