
# importing libs
import pandas as pd
import duckdb
from datetime import datetime

# reading file
data_path = '..\data\data_meli.jsonl'
df_data = pd.read_json(data_path, lines=True)


# data transformation

## include columns
df_data['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"
df_data['_data_coleta'] = datetime.now()

## transforming floats
df_data['old_price_reais'] = df_data['old_price_reais'].fillna(0).astype(float)
df_data['old_price_centavos'] = df_data['old_price_centavos'].fillna(0).astype(float)
df_data['new_price_reais'] = df_data['new_price_reais'].fillna(0).astype(float)
df_data['new_price_centavos'] = df_data['new_price_centavos'].fillna(0).astype(float)
df_data['reviews_rating_number'] = df_data['reviews_rating_number'].fillna(0).astype(float)

## removing special characters
df_data['reviews_amount'] = df_data['reviews_amount'].str.replace(r'[\(\)]', '', regex=True)
df_data['reviews_amount'] = df_data['reviews_amount'].fillna(0).astype(int)

## join of values
df_data['old_price'] = df_data['old_price_reais'] + df_data['old_price_centavos'] / 100
df_data['new_price'] = df_data['new_price_reais'] + df_data['new_price_centavos'] / 100

# romeving columns
df_data.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'], inplace=True)

# connect to db
conn = duckdb.connect(database='../data/meli.db', read_only=False)

# save data to db
df_data.to_sql('products_meli', conn, if_exists='replace', index=False)

# close conection to db
conn.close()