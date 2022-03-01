import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

df2 = pd.read_csv('Expediting 2021.csv', sep=',', index_col=None, low_memory=False)


df2['Description'] = df2['Description'].str.strip()


df2 = df2.loc[df2['Description'].isin(['APPLES','JUICE', "SUGAR", "BANANAS",
                                       "TOMATOES"])]


df2['OrdCreateDate'] = df2['OrdCreateDate'].str.slice(5,7)


df2['OrdCreateDate'].unique()

#print(df)

df2.to_excel("Expediting 2021_apples_juice.xlsx", index = False, header=True)

sns.barplot(x='OrdCreateDate', y='Delivered Qty', hue='Description', data=df2)


plt.show()
