import pandas as pd

df = pd.read_csv(
    './concert_tours_by_women.csv',
    usecols=[
        'Rank',
        'Actual gross',
        'Adjustedgross (in 2022 dollars)',
        'Artist',
        'Tour title',
        'Shows',
        'Average gross',
        'Year(s)',
    ],
)

df = df.rename(
    columns={'Adjustedgross (in 2022 dollars)': 'Adjusted gross (in 2022 dollars)'}
)

df[['Start year', 'End year']] = df['Year(s)'].str.split('-', expand=True)
df['End year'] = df['End year'].fillna(df['Start year'])
df = df.drop('Year(s)', axis=1)

aux = ['Actual gross', 'Adjusted gross (in 2022 dollars)', 'Average gross']
df[aux] = df[aux].replace(r'[^\d]', '', regex=True).astype(float)

df['Tour title'] = (
    df['Tour title']
    .replace(r'\[.*?\]|[^\w\s]', '', regex=True)
    .replace(r'\s+', ' ', regex=True)
    .str.strip()
)

df.to_csv('csv_limpo.csv', index=False)
