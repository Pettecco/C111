import numpy as np

mtz = np.random.randint(1, 10, [np.random.randint(1, 10), np.random.randint(1, 10)])

print(mtz)

linhas, colunas = mtz.shape

total = linhas * colunas

print(total)

if total & 1:
  print("A matriz pode se tornar um vetor com números impar de elementos")
else:
  print("A matriz pode se tornar um vetor com um número par de elementos")

