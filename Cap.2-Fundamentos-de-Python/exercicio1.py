name = str(input("Qual o seu nome completo? "))

# Nome em letra maiúscula
print(name.upper())
# Nome em letra minúscula
print(name.lower())

# Quantas letras tem no nome
letters = len(name) - name.count (' ')
print(letters)

name = name.replace("de Sousa", "do Inatel")
print(name)
