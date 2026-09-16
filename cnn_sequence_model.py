import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense

def build_cnn_model(sequence_length, num_features, num_classes):
    model = Sequential([
        # Сверточный слой: сканирует последовательность (например, one-hot ДНК)
        Conv1D(filters=32, kernel_size=8, activation='relu', input_shape=(sequence_length, num_features)),
        MaxPooling1D(pool_size=2),
        
        # Второй сверточный слой для более сложных паттернов
        Conv1D(filters=64, kernel_size=4, activation='relu'),
        MaxPooling1D(pool_size=2),
        
        # Переход к полносвязным слоям
        Flatten(),
        Dense(64, activation='relu'),
        Dense(num_classes, activation='softmax' if num_classes > 2 else 'sigmoid')
    ])
    
    model.compile(optimizer='adam', 
                  loss='sparse_categorical_crossentropy', 
                  metrics=['accuracy'])
    return model

if __name__ == "__main__":
    # Пример конфигурации: длина рида 100 bp, 4 нуклеотида (one-hot), 2 класса
    model = build_cnn_model(sequence_length=100, num_features=4, num_classes=2)
    model.summary()
