import numpy as np

# Функция активации, применяет сигмоидную функцию к входному значению x
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Производная сигмоиды
def sigmoid_derivative(x):
    return x * (1 - x)

# Определяем входные данные X, содержит все возможные комбинации двух бинарных входов (0 или 1)
X = np.array([[0, 0],[0, 1],[1, 0],[1, 1]])
# Определяем выходные данные Y, содержит соответствующие значения XOR
Y = np.array([[0],[1],[1],[0]])

# Инициализация весов сети
input_size = 2 #размер входного слоя (2 узла)
hidden_size = 2 #количество нейронов в скрытом слое (2 нейрона)
output_size = 1 #размер выходного слоя (1 узел)

# Установим случайные значения для весов
w1 = np.random.uniform(size=(input_size, hidden_size))
w2 = np.random.uniform(size=(hidden_size, output_size))

# Обучение нейронной сети
learning_rate = 0.1
epochs = 10000

for epoch in range(epochs):
    # Прямое распространение

    #вычисляем взвешенную сумму входов и весов
    #применяем функцию активации (сигмоида)
    #передаем результат на следующий слой
    #выход нейронной сети
    z1 = np.dot(X, w1) 
    a1 = sigmoid(z1)

    z2 = np.dot(a1, w2)
    a2 = sigmoid(z2)

    # Расчет ошибки
    error = Y - a2

    # Вычисление изменений для обратного распространения ошибки
    d_2 = error * sigmoid_derivative(a2)
    error_1 = d_2.dot(w2.T)
    d_1 = error_1 * sigmoid_derivative(a1)

    # Обновление весов
    w2 += a1.T.dot(d_2) * learning_rate
    w1 += X.T.dot(d_1) * learning_rate

# Прогнозирование
final_z1 = np.dot(X, w1)
final_a1 = sigmoid(final_z1)
final_z2 = np.dot(final_a1, w2)
final_a2 = sigmoid(final_z2)

print("тестирование кода:" , final_a2)
