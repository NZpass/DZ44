# Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?

# Даны условия задачи

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

# Вывод рандом списка робот-человек, но можно и без него.
print(data)

# Решение

data = pd.DataFrame({'whoAmI':lst})
data.loc[data['whoAmI'] == 'robot', 'Robots'] = '1'
data.loc[data['whoAmI'] != 'robot', 'Robots'] = '0'
data.loc[data['whoAmI'] == 'human', 'Humans'] = '1'
data.loc[data['whoAmI'] != 'human', 'Humans'] = '0'

# Вывод таблицы робот-человек
print(data)