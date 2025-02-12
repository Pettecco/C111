# Tuplas (Imutáveis e Heterogenea)

nomes = ('Goku', 'Vegeta', 'Trunks', 'Gohan')
print(nomes)

# Slicing de dados
print(nomes[0]) # Goku
# No Python, o primeiro indice é INCLUSIVE e no segundo é EXCLUSIVE
print(nomes[:2])
print(nomes[2:]) # Trunks, Gohan
print(nomes[1:3]) # Vegeta, Trunks
print(nomes[-1]) # Gohan


# Tentando alterar uma tupla
nomes[0] = 'Bulma'
print(nomes[0]) # TypeError: 'tuple' object does not support item assignment