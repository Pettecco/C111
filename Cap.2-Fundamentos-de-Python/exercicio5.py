num = int(input("Digite um número entre 1000 e 9999: "))

while num < 1000 or num > 9999:
  num = int(input("Digite um número entre 1000 e 9999: "))


milhar = num // 1000
unidade = num % 10
num //= 10
dezena = num % 10
num //= 10
centena = num % 10

print(f"O número tem como: \n Milhar: {milhar}\n Centena: {centena}\n Dezena: {dezena}\n Unidade: {unidade}")

