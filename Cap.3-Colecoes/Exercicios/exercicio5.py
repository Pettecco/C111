n = int(input("Digite o número de pessoas: "))

pessoas = {}

for i in range(n):
  nome = str(input("Digite o nome da pessoa: "))
  idade = int(input("Digite a idade: "))
  sexo = str(input("Digite o sexo, (M) para masculino e (F) para feminino: ")).upper()
  pessoas[nome] = {'idade': idade, 'sexo': sexo}

media = 0
mulheres_menores_20 = 0

for nome, dados in pessoas.items():
  media += dados['idade']
  if dados['sexo'] == 'F' and dados['idade'] < 20:
    mulheres_menores_20 += 1

print(f'A média de idade do grupo é {media // n} anos')
print(f'Existem {mulheres_menores_20} mulheres abaixo de 20 anos no grupo')

