link para baixar a sequencia do chromosome 1
https://www.ncbi.nlm.nih.gov/nuccore/NC_000001.11?report=genbank


1 - Primeiro passo é baixar a sequência, usando o link acima, e solta-la no diretório "chromosome1HomoSapien"

2 - dentro do diretório "chromosome1HomoSapien", pode usar o "genomeReverse.c" ou o "genomeReverseComplement" para obter o comprimento reverso da sequência.

3 - use prepareCDSs.py para separar os CDSs corretamente e organiza-los antes de serem alinados.

4 - use nonCoding.py para colher as regiões não codificante

5 - use AlingCDSs.py para alinhar todos os arquivos 

6 - use annotationGenerator.py para gerar as anotações desses arquivos.fasta