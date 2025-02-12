# Dictionaries
# São mutáveis e trabalhamo no formato chave->valor

pessoa = {'nome':'Goku', 'idade':42}
print(pessoa)

# Acessar
print(pessoa['nome'])

# Insert
pessoa['sexo'] = 'M'

# Update
pessoa['nome'] = 'Vegeta'

# Delete
del pessoa['sexo']

print(pessoa)