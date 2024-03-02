from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.dummy import DummyClassifier

#  Implemente um algoritmo de aprendizado de máquina utilizando LinearSVC para reconhecer que dada uma entrada, ela é um ser humano ou um espríto.

#  Tem corpo fisico?
#  Atravessa parede?
#  Tem consciencia?
#  Já morreu?
#  Pode falar?

catalogo = {
    1 : "Humano",
    2 : "Espirito"
}

humano1 =  [1,0,1,0,1]
humano2 =  [1,0,0,1,0]
humano3 =  [1,0,0,0,0]


espirito1 = [0,1,1,1,1]
espirito2 = [0,1,0,1,0]
espirito3 = [0,1,0,1,0]

treino_x=[humano1,humano2,humano3,espirito1,espirito2,espirito3]

treino_y = [1, 1, 1, 0, 0, 0]

modelo = LinearSVC()


modelo.fit(treino_x,treino_y)

print("Digite 1 para sim e 0 para não")
corpo_fisico = input("O indivuduo tem corpo fisico?")
atravessa_parede = input("O indivuduo atravessa parede")
consciencia = input("O indivuduo tem consciencia?")
ja_morreu = input("O indivuduo ja morreu?")
pode_falar = input("O indivuduo pode falar?")
 
individuo_misterioso = [int(corpo_fisico), int(atravessa_parede), int(consciencia), int(ja_morreu), int(pode_falar)]

resultado = modelo.predict([individuo_misterioso])
if(resultado == 0) :
    print("O Bicho é humano, pode confiar")
if(resultado == 1):
    print("O bicho é fantasmagolico")


