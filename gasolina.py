import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

gasolina = df[['dia', 'venda']].groupby('dia').agg('sum').reset_index()
gasolina.head()

with sns.axes_style('whitegrid'):

  fig, ax = plt.subplots(figsize=(8, 5))
  sns.lineplot(data=gasolina, x='dia', y='venda', color='r', ax=ax)
  ax.set(title='Variação do preço da gasolina ao longo dos dias', xlabel='Dia', ylabel='Preço (R$)');

plt.savefig('gasolina.png')
plt.show()