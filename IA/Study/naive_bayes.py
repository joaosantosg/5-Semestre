import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
# Criando o dataframe de exemplo
dados = {
    'temperatura': [30, 25, 28, 18, 20, 22, 24, 28, 26, 30],
    'umidade': [85, 90, 78, 65, 75, 70, 80, 75, 80, 70],
    'jogar_tenis': ['Não', 'Não', 'Sim', 'Sim', 'Sim', 'Sim', 'Não', 'Sim', 'Sim', 'Não']
}

df = pd.DataFrame(dados)
print(df)

# Separando as variáveis de entrada (temperatura e umidade) e o alvo (jogar_tenis)
X = df[['temperatura', 'umidade']]
y = df['jogar_tenis']

# Dividindo o conjunto de dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = GaussianNB()
modelo_svc = LinearSVC()

modelo_svc.fit(X_train, y_train)

predicao_svc = modelo_svc.predict(X_test)

acuaria_svc = accuracy_score(y_test, predicao_svc)


print("Acuracia svc", acuaria_svc)
modelo.fit(X_train, y_train)

y_predicao = modelo.predict(X_test)

acuaria = accuracy_score(y_test, y_pred=y_predicao)

print("Acuracia", acuaria)