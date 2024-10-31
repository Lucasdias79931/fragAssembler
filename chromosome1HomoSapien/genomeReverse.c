#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct{
    char header[100];
    char *sequence;
}Sec;

int max = 500;

Sec *getSec(char *from_directory) {
    FILE *file = fopen(from_directory, "r");
    if (file == NULL) {
        perror("Erro ao abrir o arquivo");
        exit(1);
    }

    Sec *Sequence = (Sec *)malloc(sizeof(Sec));
    if (Sequence == NULL) {
        perror("Erro ao alocar memória para Sequence");
        fclose(file);
        exit(1);
    }

    if (fgets(Sequence->header, sizeof(Sequence->header), file) == NULL) {
        perror("Erro ao ler o header");
        free(Sequence);
        fclose(file);
        exit(1);
    }

    Sequence->sequence = (char *)malloc(sizeof(char) * max);
    if (Sequence->sequence == NULL) {
        perror("Erro ao alocar memória para Sequence->sequence");
        free(Sequence);
        fclose(file);
        exit(1);
    }

    int inter = 0;
    int ch;
    while ((ch = fgetc(file)) != EOF) {
        Sequence->sequence[inter++] = ch;

        if (inter == max) {
            max *= 2;
            char *tmp = (char *)realloc(Sequence->sequence, sizeof(char) * max);
            if (tmp == NULL) {
                perror("Erro ao redimensionar");
                free(Sequence->sequence);
                free(Sequence);
                fclose(file);
                exit(1);
            }
            Sequence->sequence = tmp;
        }
    }

    Sequence->sequence[inter] = '\0';  
    
    fclose(file);

    return Sequence;
}



void reverseSequence(char *sequence) {
    int length = strlen(sequence);
    int i = 0, j = length - 1;

    while (i <= j) {
        // Complemento e inversão simultâneos
        char temp_i = sequence[i];
        char temp_j = sequence[j];

        // Complemento
        switch (temp_i) {
            case 'A': temp_i = 'T'; break;
            case 'T': temp_i = 'A'; break;
            case 'C': temp_i = 'G'; break;
            case 'G': temp_i = 'C'; break;
        }

        switch (temp_j) {
            case 'A': temp_j = 'T'; break;
            case 'T': temp_j = 'A'; break;
            case 'C': temp_j = 'G'; break;
            case 'G': temp_j = 'C'; break;
        }

        // Inversão
        sequence[i] = temp_j;
        sequence[j] = temp_i;

        i++;
        j--;
    }
}

void writeSequence(Sec *sequence, char *to_directory) {
    FILE *file = fopen(to_directory, "w");
    if (file == NULL) {
        perror("Erro ao abrir o arquivo");
        exit(1);
    }
    fprintf(file, "%s\n", sequence->header);
    fprintf(file, "%s\n", sequence->sequence);
    fclose(file);
}



int main(){
    
    clock_t start = clock();
    
    printf("pegando a sequência\n");
    Sec *sequence = getSec("sequence.fasta");
    printf("Sequência colhida com sucesso\n");
    
    printf("Iniciando a reversão do complemento\n");

    reverseSequence(sequence->sequence);

    printf("Reversão concluida\n");
    
    
    
    printf("Salvando em arquivo\n");
    
    writeSequence(sequence, "reversedSequence.fasta");
    printf("Arquivo salvo com sucesso\n");

    clock_t end = clock();
    double tempo_execucao = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Tempo de execução: %.2f segundos\n", tempo_execucao);

    return 0;
}