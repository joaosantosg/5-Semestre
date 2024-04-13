class AnimalClassifier:
  def __init__(self):
    self.rules = {
        'Possui penas?': {'s': 'Pássaro', 'n': None},
        'Vive na água?': {'s': 'Peixe', 'n': None},
        'Possui pelos ou cabelos?': {'s': 'Mamífero', 'n': None},
        'Possui escamas?': {'s': 'Réptil', 'n': None},
        'Vive em ambientes aquáticos e terrestres?': {'s': 'Anfíbio', 'n': None}
    }

  def classify(self, animal_features):
    for question, answers in self.rules.items():
      answer = animal_features.get(question)
      if answer in answers:
        classification = answers[answer]
        if classification:
          return classification
    return 'Indefinido'

# Set do database
database = [
    {'Nome': 'Papagaio', 'Possui penas?': 's'},
    {'Nome': 'Tubarão', 'Vive na água?': 's'},
    {'Nome': 'Gato', 'Possui pelos ou cabelos?': 's'},
    {'Nome': 'Cobra', 'Possui escamas?': 's'},
    {'Nome': 'Sapo', 'Vive em ambientes aquáticos e terrestres?': 's'},
    {'Nome': 'Pinguim', 'Possui penas?': 's'},
]

# Intanciar o classificador
classifier = AnimalClassifier()

# Treinamento e validação
correct_predictions = 0
for animal in database:
  animal_name = animal['Nome']
  actual_class = input(f"Qual a classificação do animal {animal_name}? ")
  predict_class = classifier.classify(animal)
  if actual_class.lower() == predict_class.lower():
    correct_predictions += 1
  print (f"Classificação prevista para {animal_name}: {predict_class}")

# Calcular a acurácia
total_animals = len(database)
accuracy = (correct_predictions / total_animals) *100
print (f"A acurácia do classificador é: {accuracy}%")
