print("-----------Tabuada de um intervalo de X a Y-----------")

x = int(input("Digite x: "))
y = int(input("Digite y: "))

for i in range(x, y+1):
  fator = 1
  while fator <= 10:
    print(f'{i} x {fator} = {i*fator}')
    fator += 1
  print('\n')

