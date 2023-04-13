import numpy as np
import pandas as pd
from statsmodels.stats.weightstats import ztest
import random

chat_id = 416934694 # Ваш chat ID, не меняйте название переменной

def solution(x:np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы

    if ztest(x,300)[1] < 0.04:
        return True
    else:
        return False
