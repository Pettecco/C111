km = float(input("Qual a distancia em KM da viagem? "))

if km > 200:
  print(f"O preço da da passagem é R${km*0.45}")
else:
  print(f"O preço da passagem é R${km*0.50}")