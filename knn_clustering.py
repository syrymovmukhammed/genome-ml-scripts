import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def run_knn():
    df = pd.read_csv('samples_data.csv')
    
    # Пример предварительной обработки Pandas: группировка дубликатов измерений по ID и усреднение
    df = df.groupby('sample_id').agg('mean').reset_index()
    
    X = df.drop(columns=['sample_id', 'phenotype'])
    y = df['phenotype']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Инициализация kNN (ищем 5 ближайших соседей)
    knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
    
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Точность kNN модели: {accuracy:.2f}")

if __name__ == "__main__":
    run_knn()
