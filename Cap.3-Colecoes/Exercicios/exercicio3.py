nome = str(input('Digite o nome do aluno: '))
nota = float(input('Qual a média do aluno: '))

dados = {'nome': nome, 'media': nota}

if(dados['media'] >= 50):
  print(f'A situação do aluno {dados['nome']} é: APROVADO!')
else:
  print(f'A situação do aluno {dados['nome']} é: REPROVADO!')

print(dados)
