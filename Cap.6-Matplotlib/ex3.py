import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('space.csv', delimiter=';')       

roscosmos_df = df[df['Company Name'] == 'Roscosmos']

status_missoes = roscosmos_df['Status Mission'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(status_missoes, labels=status_missoes.index, autopct='%1.1f%%', colors=['red', 'blue', 'yellow'])
plt.title('Porcentagem de Missões da Roscosmos (Sucesso vs. Falha)')
plt.show()