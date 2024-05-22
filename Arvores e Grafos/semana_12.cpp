// Joao Victor Guimaraes Santos
// Matricula: 2212057
// Disciplina: Arvores e Grafos - 2024/01

#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* left;
    struct Node* right;
} Node;

Node* newNode(int data) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

Node* insertNode(Node* root, int data) {
    if (root == NULL) {
        return newNode(data);
    } else {
        if (data <= root->data) {
            root->left = insertNode(root->left, data);
        } else {
            root->right = insertNode(root->right, data);
        }
        return root;
    }
}

int height(Node* root) {
    if (root == NULL) {
        return -1;
    } else {
        int leftHeight = height(root->left);
        int rightHeight = height(root->right);
        if (leftHeight > rightHeight) {
            return leftHeight + 1;
        } else {
            return rightHeight + 1;
        }
    }
}

void printLeaves(Node* root) {
    if (root == NULL) {
        return;
    }
    if (root->left == NULL && root->right == NULL) {
        printf("%d ", root->data);
    }
    printLeaves(root->left);
    printLeaves(root->right);
}

int rootDegree(Node* root) {
    if (root == NULL) {
        return 0;
    }
    int degree = 0;
    if (root->left != NULL) {
        degree++;
    }
    if (root->right != NULL) {
        degree++;
    }
    return degree;
}

void preOrderTraversal(Node* root) {
    if (root == NULL) {
        return;
    }
    printf("%d ", root->data);
    preOrderTraversal(root->left);
    preOrderTraversal(root->right);
}

void inOrderTraversal(Node* root) {
    if (root == NULL) {
        return;
    }
    inOrderTraversal(root->left);
    printf("%d ", root->data);
    inOrderTraversal(root->right);
}

void postOrderTraversal(Node* root) {
    if (root == NULL) {
        return;
    }
    postOrderTraversal(root->left);
    postOrderTraversal(root->right);
    printf("%d ", root->data);
}

int main() {
    int elements[] = {55, 12, 49, 11, 9, 87, 45, 75, 2, 4, 1, 34, 42, 17, 31, 28, 49, 98, 91, 77, 82, 63, 37};
    int num_elements = sizeof(elements) / sizeof(elements[0]);

    Node* root = NULL;

    // Construindo a árvore
    for (int i = 0; i < num_elements; i++) {
        root = insertNode(root, elements[i]);
    }

    printf("Arvore preenchida:\n");
    printf("Pre-ordem: ");
    preOrderTraversal(root);
    printf("\nEm-ordem: ");
    inOrderTraversal(root);
    printf("\nPos-ordem: ");
    postOrderTraversal(root);

    printf("\nAltura da arvore: %d\n", height(root));

    printf("Nos folhas: ");
    printLeaves(root);
    printf("\n");

    // Grau da raiz
    printf("Grau da raiz: %d\n", rootDegree(root));

    return 0;
}
