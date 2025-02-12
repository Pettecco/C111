# Listas (Mutável e composta)

nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']

# INSERT
nomes.append('Bulma') # Insere no final
nomes.insert(2, 'Piccolo') # Insere em uma posição específica
print(nomes)

# UPDATE
nomes[0] = 'Goten'

# DELETE
del nomes[1] # Excluindo pelo índice / nomes.pop(1)
nomes.remove('Trunks') # Excluindo pelo valor (o valor precisa existir na lista)
print(nomes)

if 'Piccolo' in nomes:
  print('Piccolo is here!!')

nomes.sort()
print(nomes)
