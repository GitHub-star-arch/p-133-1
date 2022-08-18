from matplotlib.pyplot import axis
import pandas as pd

df = pd.read_csv('dwarfstars.csv')

df=df.dropna()
df.drop(['Unnamed: 0'],axis=1,inplace=True)

df['radius'] = df['radius']*0.102763
df['mass'] = df['mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df['mass'] = df['mass']*0.000954588

df.reset_index(drop=True,inplace=True)

print(df.dtypes)
print(df.head())

df.to_csv('dwarfstars_converted.csv')