import pandas as pd
import numpy as np

# Ao se criar um novoa DataFrame, três infomrações primoridiais precisam ser passadas:
# -> Uma coleção de labels
# -> Uma coleção de columns
# -> Uma coleção de 2-D (matriz) de dados

np.random.seed(10)

df = pd.DataFrame(
  index=['A', 'B', 'C', 'D', 'E'],
  columns=['W', 'X', 'Y', 'Z'],
  data=np.random.randint(1, 50, [5, 4])
)
print(df)

# Cada coluna de um DataFrame é uma Series
# Acessando uma coluna
print(df['W'])
print(type(df['W']))

# Acessando múltiplas colunas
print(df[['W', 'Z']])
# Acessando um valor específico
print(df['W']['A'])


# Slicing de dados podem ser facilmente realizados por meio das funções loc() e iloc()
# Ambas produzem o mesmo resultado, porém uma leva em condideração os nomes dos índices e a outra os índices numérics
print(df.loc[['A', 'B'], ['X', 'Y', 'Z']])
print(df.iloc[0:2, 1:])


