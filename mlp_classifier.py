import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

def run_mlp():
    # Загрузка и подготовка данных
    # Предполагается, что в 'expression_data.csv' есть колонки с генами и колонка 'target'
    df = pd.read_csv('expression_data.csv')
    
    X = df.drop(columns=['target'])
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Инициализация классической полносвязной нейросети
    mlp = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)
    
    print("Обучение модели...")
    mlp.fit(X_train, y_train)
    
    print("Оценка качества:")
    predictions = mlp.predict(X_test)
    print(classification_report(y_test, predictions))

if __name__ == "__main__":
    run_mlp()
