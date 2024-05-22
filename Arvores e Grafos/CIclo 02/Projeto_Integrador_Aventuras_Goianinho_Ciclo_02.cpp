// Aventuras de Goianinho 
// Ciclo 02
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Estrutura para um nó da árvore binária
typedef struct Node {
    char *descricao;
    struct Node *esquerda;
    struct Node *direita;
} Node;

// Função para criar um novo nó da árvore binária
Node* criarNo(char *descricao) {
    Node *novoNo = (Node*)malloc(sizeof(Node));
    novoNo->descricao = strdup(descricao);
    novoNo->esquerda = NULL;
    novoNo->direita = NULL;
    return novoNo;
}

// Função para liberar a memória alocada para a árvore binária
void liberarArvore(Node *raiz) {
    if (raiz != NULL) {
        liberarArvore(raiz->esquerda);
        liberarArvore(raiz->direita);
        free(raiz->descricao);
        free(raiz);
    }
}

// Função para exibir a árvore binária em ordem
void exibirArvore(Node *raiz) {
    if (raiz != NULL) {
        exibirArvore(raiz->esquerda);
        printf("%s\n", raiz->descricao);
        exibirArvore(raiz->direita);
    }
}

// Função para simular interação do jogador com a árvore binária
void interagir(Node *no) {
    printf("Você está em: %s\n", no->descricao);
    if (no->esquerda != NULL || no->direita != NULL) {
        printf("Escolha uma opção:\n");
        if (no->esquerda != NULL) {
            printf("1. %s\n", no->esquerda->descricao);
        }
        if (no->direita != NULL) {
            printf("2. %s\n", no->direita->descricao);
        }
        int escolha;
        do {
            printf("Opção escolhida: ");
            scanf("%d", &escolha);
            if (escolha != 1 && escolha != 2) {
                printf("Opção inválida. Escolha novamente.\n");
            }
        } while (escolha != 1 && escolha != 2);
        if (escolha == 1) {
            interagir(no->esquerda);
        } else {
            interagir(no->direita);
        }
    } else {
        printf("Fim da aventura!\n");
    }
}

int main() {
    // Construção da árvore binária de decisão
    Node *raiz = criarNo("Introdução: Apresentação dos personagens principais, Goianinho e Pamonhito, e do objetivo da jornada.");
    raiz->esquerda = criarNo("Cerrado Vegetação e Animais: Os jogadores exploram as diferentes plantas e animais típicos do cerrado.");
    raiz->direita = criarNo("Cultura Goiana: Neste ramo, os jogadores aprendem sobre os costumes, tradições e festivais do povo goiano.");
    raiz->esquerda->esquerda = criarNo("ipê-amarelo, ema, tamanduá-bandeira");
    raiz->esquerda->direita = criarNo("tatu canastra, lobo guará, seriema");
    raiz->direita->esquerda = criarNo("Festa do Divino Espírito Santo, Cavalhada");
    raiz->direita->direita = criarNo("História e Geografia: Os jogadores desvendam charadas e enigmas relacionados à história e geografia de Goiás.");

    // Exibindo a árvore binária
    printf("Estrutura da Árvore Binária:\n");
    exibirArvore(raiz);

    // Simulação de interação do jogador com a árvore binária
    printf("\n---\n");
    interagir(raiz);

    // Liberando memória alocada para a árvore binária
    liberarArvore(raiz);

    return 0;
}
