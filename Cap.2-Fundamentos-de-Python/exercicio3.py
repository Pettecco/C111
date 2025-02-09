print("Qual seu sexo?")
gender = str(input("Digite M para masculino ou F para feminino: "))

while gender != 'M' and gender != 'F':
  gender = str(input("Digite M para masculino ou F para feminino: "))

if gender == 'F':
  print("Você é do sexo feminino")
else:
  print("Você é do sexo masculino")

