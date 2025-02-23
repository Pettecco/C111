# Mini campo minado
import numpy as np

field = np.zeros([2, 2], dtype=int)

randomColumn = np.random.randint(0, 2)
randomLine = np.random.randint(0, 2)

field[randomLine][randomColumn] = 1 

field_mask = [['*', '*'], ['*', '*']]
count_sucessfull_moves = 0

def print_mask(mask):
    for row in mask:
        print(" ".join(str(cell) for cell in row))

while True:
    
    if(count_sucessfull_moves == 3):
      print("Congratulations! You beat the game! :)")
      break
    
    print("Selecione uma posição x e y da matriz (0 ou 1):")
    print_mask(field_mask)


    x = int(input("Digite o valor de x (linha): "))
    y = int(input("Digite o valor de y (coluna): "))
    

    if field[x][y] == 1:
        print("Game Over! :( Try again!")
        break
    else:
        field_mask[x][y] = '0'
        count_sucessfull_moves += 1




