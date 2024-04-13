# Você foi contratado por uma empresa de comércio eletrônico para desenvolver um sistema de classificação de produtos com base em suas características. O objetivo é criar um algoritmo simples que utilize classificação por regras para determinar a categoria de um produto entre cinco possíveis: eletrônicos, roupas, alimentos, livros e utensílios domésticos.

# O algoritmo deve fazer uma série de perguntas ao usuário sobre as características do produto, como seu uso, composição, categoria de venda, entre outras. Com base nas respostas fornecidas, o algoritmo deverá classificar o produto em uma das categorias mencionadas.

# As regras para a classificação são as seguintes:

# Se o produto é um dispositivo eletrônico, como computador, celular ou televisão, será classificado como eletrônico.
# Se o produto é uma peça de vestuário, como camisa, calça ou sapato, será classificado como roupa.
# Se o produto é um alimento, bebida ou ingrediente culinário, será classificado como alimento.
# Se o produto é um livro, revista ou qualquer outro material de leitura, será classificado como livro.
# Se o produto é um utensílio de cozinha, decoração ou limpeza doméstica, será classificado como utensílio doméstico.
# Se nenhuma das condições acima for atendida, o produto será classificado como "Indefinido".
# Desenvolva um algoritmo em Python que implemente o classificador de produtos conforme as regras especificadas. Após a implementação, teste o algoritmo com diferentes exemplos de produtos e verifique se as classificações estão corretas.

from unidecode import unidecode

class Classificador():
    def __init__(self):
        self.rules = {
            "O produto precisa de energia para funcionar?" : {"s": "eletrônico", "n": None},
            "O produto é de vestir?": {"s": "vestuário", "n": None},
            "O produto é de comer?": {"s": "alimento", "n": None},
            "O produto é destinado a leitura?": {"s": "livro", "n":None},
            "O produto pode ser utilizado para preparar alimentos?" : {"s":"utensílio de cozinha", "n":None },
        }

    def classify(self, elementos):
        for pergunta,conjunto_respostas in self.rules.items():
            resposta = elementos.get(pergunta)
            if resposta in conjunto_respostas:
                classificacao = conjunto_respostas[resposta]
                if classificacao:
                    return classificacao
                else:
                    return "Indefinido"
            else:
                return "Indefinido"
            

dataset = [
    {"Produto": 'Notebook', "O produto precisa de energia para funcionar?": "s"},
    {"Produto": "Camiseta", "O produto é de vestir?": "s"},
    {"Produto": "Pastel de Flango", "O produto é de comer?":"s"},
    {"Produto": "Dom Casmurro", "O produto é destinado a leitura?": "s"},
    {"Produto": "Ovo", "O produto pode ser utilizado para preparar alimentos?": "s"},
    {"Produto": "Peruca", "O produto é de vestir": "n"}
]


classificador_objetos = Classificador()
predicoes_corretas = 0
print("A seguir voce deve classificar os produtos entre as seguintes categorias:")
print("eletrônico")
print("vestuário")
print("alimento")
print("livro")
print("utensílio de cozinha\n")


for objeto in dataset:
    produto = objeto['Produto']
    categoria_input = input(f'Qual a categoria do produto {produto}?')

    categoria_predita = classificador_objetos.classify(objeto)

    if(unidecode(categoria_input.lower()) == unidecode(categoria_predita.lower())):
        predicoes_corretas +=1
        print(f"O algoritimo acertou o objeto {produto} pertence a categoria {categoria_predita}")
    print(f"A categoria predita pelo algoritimo foi {categoria_predita}")

total_objetos = len(dataset)
accuracy = (predicoes_corretas / total_objetos) *100
print (f"A acurácia do classificador é: {accuracy}%")