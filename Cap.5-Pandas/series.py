import pandas as pd
import numpy as np

s1 = pd.Series({'a': 10, 'b': 20, 'c': 30})
s2 = pd.Series({'a': 10, 'c': 50, 'd': 80})

print(s1 + s2)

print(s1.add(s2, fill_value=0))

# Funçõos do numpy
print(np.mean(s1))
print(s1[['a', 'c']])

# Slicing
print(s1[1:])

# Condicionais
print(s1[s1 > 25])
print(s1[s1 > s1.mean()])
print(s1[s1/2 == 10])