import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./csv_limpo.csv')

q1 = (
    df.groupby('Artist')
    .filter(lambda x: len(x) == df['Artist'].value_counts().max())
    .groupby('Artist')['Actual gross']
    .mean()
    .reset_index()
    .sort_values('Actual gross', ascending=False)
    .head(1)
    .iloc[0]['Artist']
)

q2 = (
    df[df['Start year'] == df['End year']]
    .nlargest(1, 'Average gross')
    .iloc[0]['Tour title']
)

q3 = (
    df.assign(show_unitario = df['Adjusted gross (in 2022 dollars)'] / df['Shows'])
    .sort_values('show_unitario', ascending=False)
    .head(3)
    [['Artist', 'Tour title', 'show_unitario']]
    .rename(columns={'show_unitario': 'Show unitario'})
    .reset_index(drop=True)
)

with open('/app/volume/respostas.txt', mode='w') as saida:
    saida.write(f'Q1: \n\n--- A artista que mais aparece nessa lista e possui a maior média de seu faturamento bruto é {q1}\n\n')
    saida.write(f'Q2: \n\n--- Das turnês que aconteceram dentro de um ano, qual a turnê com a maior média de faturamento bruto é {q2}\n\n')
    saida.write(f'Q3: \n\n--- As três turnês que tiveram os shows mais lucrativos foram: {q3["Tour title"].iloc[0]} de {q3['Artist'].iloc[0]}, com o show unitário avaliado em US${q3["Show unitario"].iloc[0]:.2f}, {q3["Tour title"].iloc[1]} de {q3['Artist'].iloc[1]}, com o show unitário avaliado em US${q3["Show unitario"].iloc[1]:.2f}, e {q3["Tour title"].iloc[2]} de {q3['Artist'].iloc[2]}, com show unitário avaliado em US${q3["Show unitario"].iloc[2]:.2f}.\n\n')

q4 = (
    df
    .groupby('Artist')
    .filter(lambda x: len(x) == df['Artist'].value_counts().max())
    .groupby('Artist')['Actual gross']
    .sum()
    .pipe(lambda x: df[df['Artist'] == x.idxmax()])
)

plt.figure(figsize=(14, 8))

sns.lineplot(data=q4, x='Start year', y='Actual gross', marker='o')
plt.title(f'Faturamento Bruto por Início de Tour da artista "{q4["Artist"].iloc[0]}"')
plt.xlabel('Ano de Início da Tour')
plt.ylabel('Faturamento Bruto em Dólares')
plt.gca().yaxis.set_major_formatter('${x:,.0f}')
plt.savefig('/app/volume/Q4.png', dpi=300, bbox_inches='tight')
plt.close()

q5 = (
    df
    .groupby('Artist')['Shows']
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

plt.figure(figsize=(14, 8))

sns.barplot(data=q5, x='Shows', y='Artist', hue='Artist')
plt.title('Top 5 Artistas por Número de Shows')
plt.xlabel('Número de Shows')
plt.ylabel('Artistas')
plt.savefig('/app/volume/Q5.png', dpi=300, bbox_inches='tight')
plt.close()