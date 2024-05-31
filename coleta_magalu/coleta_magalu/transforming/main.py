
# importing libs
import pandas as pd
import duckdb
from datetime import datetime

# reading file
data_path = '..\data\data_magalu.jsonl'
df_data = pd.read_json(data_path, lines=True)

# data transformation

## include columns
df_data['dt_coleta'] = datetime.now()

## removing special characters
df_data['price_of'] = df_data['price_of'].str.replace('R$\xa0', '').str.replace(',', '.').fillna(0)
df_data['price_per'] = df_data['price_per'].str.replace('R$\xa0', '').str.replace(',', '.').fillna(0)

# connect to db
conn = duckdb.connect(database='../data/magalu.db', read_only=False)

# save data to db
df_data.to_sql('products_magalu', conn, if_exists='replace', index=False)

# close conection to db
conn.close()