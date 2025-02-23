import numpy as np

arr1 = np.ones([8], dtype=int)
arr2 = np.random.randint(0, 9, [8])

arr3 = arr1 + arr2

sum = np.sum(arr3)
print(sum)

if sum >= 40:
  arr3 = np.reshape(arr3, (4, 2)) # mais linhas que colunas
else:
  arr3 = np.reshape(arr3, (2, 4)) # mais colunas que linhas

print(arr3)