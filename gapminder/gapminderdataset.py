import pandas
df = pandas.read_csv('gapminder.csv')
print(df.head())
print(type(df))
print(df.shape)
# get column names
print(df.columns)
print(df.dtypes)
print(df.info())
# just get the country column and save it to its own variable
country_df = df['country']
print(country_df.head())
# show the last 5 observations
print(country_df.tail())
country_df_dot = df.country
print(country_df_dot.head())
# Looking at country, continent, and year
subset = df[['country', 'continent', 'year']]
print(subset.head())
print(subset.tail())
subset = df.iloc[:, 0]
print(subset.head())

