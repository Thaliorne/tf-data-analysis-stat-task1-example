import pandas as pd
import numpy as np


chat_id = 259636079 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
  def solution(x: np.array) -> float:
    data = x - 307
    data = np.log(data)
    mu_est_list = []
    mean_mu_est_list = []
    for i in range(10000):
        mu_est_list.append(pd.Series(data).sample(5,replace=True).mean())      
    x = np.array(mu_est_list)
    return x.mean() # Ваш ответ
