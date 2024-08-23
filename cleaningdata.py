#melakukan import libraries pandas
import pandas as pd

#membaca file cvs
df = pd.read_csv('carsales.csv', encoding='latin1')
df

#ubah nama kolom menjadi huruf kecil semua
df.columns = df.columns.str.lower()
df.columns


# Mengubah nama kolom (customer name, annual income, dan body style dengan mengganti spasi dengan '_' ) dengan spasi menjadi underscore
df.rename(columns=lambda x: x.replace(' ', '_') if x in ['customer name', 'annual income', 'body style'] else x, inplace=True)
df.head(5)

#melakukan cek duplikasi data
df.duplicated().sum()

# cek missing value
df.isna().sum()

#mendelete missing value
df.dropna(inplace=True) 


