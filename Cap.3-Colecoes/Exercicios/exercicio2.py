loja1 = {'Xiomi Redmi 8', 'Samsung Galaxy S10', 'Iphone 13', 'Motorola Moto G'}
loja2 = {'Iphone 13', 'Samsung Galaxy A30', 'Motorola Moto G', 'Xiomi Redmi 9C'}

total_modelos = loja1 | loja2

print("Você possui os seguintes modelos disponíveis no total: ")
print(total_modelos)
print(f"Totalizando um total de: {len(total_modelos)} modelos")