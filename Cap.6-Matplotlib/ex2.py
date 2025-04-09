import pandas as pd                     
import matplotlib.pyplot as plt         

df = pd.read_csv('space.csv', delimiter=';')       

usa_empresas = df[df['Location'].str.contains('USA')]
china_empresas = df[df['Location'].str.contains('China')]

usa_empresas_unicas = usa_empresas['Company Name'].unique()
china_empresas_unicas = china_empresas['Company Name'].unique()

num_usa = len(usa_empresas_unicas)
num_china = len(china_empresas_unicas)


countries = ['USA', 'China']         
empresas = [num_usa, num_china]        

plt.figure(figsize=(8, 6))

plt.bar(countries, empresas, color=['blue', 'red'])

plt.xlabel('País')
plt.ylabel('Número de empresas')
plt.title('Número de empresas espaciais nos USA e China')

plt.show()