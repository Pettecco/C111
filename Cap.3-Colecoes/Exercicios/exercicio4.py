dados = {}

for i in range(3):
  nome = str(input(f'Digite o nome da pessoa {i+1}: '))
  peso = float(input(f'Digite o peso da pessoa {i+1}: '))
  dados[nome] = peso

nome_leve = nome_pesado = list(dados.keys())[0]
peso_leve = peso_pesado = dados[nome_leve]

for nome, peso in dados.items(): # É possivel fazer um tipo de desestruturação com o .items()
  if peso < peso_leve:
    nome_leve = nome
    peso_leve = peso
  elif peso > peso_pesado:
    nome_pesado = nome
    peso_pesado = peso

print(f'A pessoa mais pesada é: {nome_pesado}, pesando {peso_pesado} KG')
print(f'A pessoa mais leve é: {nome_leve}, pesando {peso_leve} KG')




