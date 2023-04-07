import pandas as pd
import numpy as np


chat_id = 259636079 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    data = x
    # Определяем функцию для оценки коэффициента x
    def estimate_x(data):
        # Оцениваем параметры распределения
        mu = np.mean(np.log(data) - 307)
        sigma = np.std(np.log(data) - 307)

        # Возвращаем оценку коэффициента x
        return np.exp(307 + sigma**2 / 2)

    # Определяем функцию для bootstrap
    def bootstrap(data, n_samples=1000, sample_size=None):
        if sample_size is None:
            sample_size = len(data)
        samples = np.random.choice(data, size=(n_samples, sample_size), replace=True)
        return samples

    # Выполняем bootstrap и оцениваем коэффициент x на каждой выборке
    samples = bootstrap(data)
    x = np.array([estimate_x(sample) for sample in samples])
    
    return x.mean() # Ваш ответ
