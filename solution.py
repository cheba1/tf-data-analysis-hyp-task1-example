import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha=0.02
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    p_combined = (x_success + y_success) / (x_cnt + y_cnt)
    z_value = (p1 - p2) / sqrt(p_combined * (1 - p_combined) * (1 / x_cnt + 1 / y_cnt))
    if abs(z_value) > norm.ppf(1 - alpha / 2):
        return True  # отвергаем H0
    else:
        return False  # не отвергаем H0
    
