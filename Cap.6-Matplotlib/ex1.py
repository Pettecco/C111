import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('paises.csv', sep = ";")
dfAmerica = dataset[dataset['Region'].str.contains('NORTHERN AMERICA', case = False)]

plt.figure(figsize=(12, 6))
plt.plot(dfAmerica['Country'], dfAmerica['Birthrate'], label='Birthrate', marker='o')
plt.plot(dfAmerica['Country'], dfAmerica['Deathrate'], label='Deathrate', marker='o')

plt.xticks(rotation=45)
plt.title('Birthrate and Deathrate in Northern America')   
plt.xlabel('Countries')
plt.ylabel('Rate (%)')
plt.legend()
plt.grid(True)
plt.show()