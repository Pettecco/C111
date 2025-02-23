import numpy as np

np.random.seed(10)

mtz = np.random.randint(1, 50, [4, 4])

media_linhas = mtz.sum(axis=1)/4
print(media_linhas)
media_colunas = mtz.sum(axis=0)/2
print(media_colunas)
# Maior valor da média das linhas
print(media_linhas.max())
# Maior valor da média das colunas
print(media_colunas.max())

import numpy as np

count = np.unique(mtz, return_counts=True)

print('\nOcorrência dos valores da matriz:')
for i in range(len(count[1])):
   print(f'{count[0][i]}: {count[1][i]}')

print('\nValores que apareceme exatamente 2 vezes:')
for i in range(len(count[1])):
    if count[1][i] == 2:  
      print(count[0][i]) 
